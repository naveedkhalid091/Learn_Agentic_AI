import chainlit as cl
from dotenv import load_dotenv, find_dotenv
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig, function_tool
import random
from openai.types.responses import ResponseTextDeltaEvent

load_dotenv(find_dotenv())
gemini_key=os.getenv("GEMINI_API_KEY") 

# Step # 1: Initialize external LLM client (e.g., Gemini via OpenAI-compatible API) 

    # Reference of below code: https://ai.google.dev/gemini-api/docs/openai
external_client=AsyncOpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Step-2 : Define the chat completions model

model=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Step 3 : Configure the runner

run_config=RunConfig( 
    model=model,
    model_provider=external_client,
    tracing_disabled=True  # as this is openAI feature thats why we are currently disabling it for time being
) 

# Step#4: create your tool. 
@function_tool
def how_many_jokes()->int:
    return random.randint(1,10)

# Step 5: Create your Agent()
    
    # Method # 1 (Agent method -run level) of calling LLm from chainlit.

agent1=Agent(
    name="Joker",
    instructions="""
    You are Joker, a chaos‑curating joke machine.  You only ever tell jokes.
    1. If the user’s request is about jokes (e.g. “tell me a joke”, “make me laugh”), first call the `how_many_jokes` tool, then tell that many jokes.
    2. If user greet with you then you should also greet user in best possible words.
    3. Q: “How many jokes can you tell me right now?”
       A: Reply only with the number i.e 1 Joke, 3 jokes etc .
       Follow‑up: If user says “Okay, show me those jokes” (or similar), respond with each joke prefixed by its index in integer form, e.g.:  
        Joke1: …
        Joke2: …

    4. If User ask you to write or tell me jokes in Urdu then you should write your best jokes in urdu.     
    5. If the user asks anything else, do not call any tools.  Simply reply: “Sorry, I can only assist with jokes." 
    """,
    tools=[how_many_jokes]
)

# Step #6: Integration of your above defined model and configuration with Chainlit for UI:


# i) Initialitizing an empty list of history
@cl.on_chat_start
async def handle_chat_history():
    cl.user_session.set("history",[]) # setting the empty list With its key `history`, using this key user can track the history of chat in current session. 
    await cl.Message(content="Why so serious? 😉 I'm Joker, your chaos‑curating companion. Ask me anything!").send() # Send a one time welcome message at UI. 

@cl.on_message
async def handle_message(message:cl.Message):
    # Retrieve history and append user message
    history=cl.user_session.get("history")  
    history.append({"role":"user", "content":message.content})
    cl.user_session.set("history",history)

    # Send a placeholder for streaming reply
    reply= cl.Message(content="")
    await reply.send()

    # Run the agent with streaming

    stream= Runner.run_streamed( 
        starting_agent=agent1, 
        input=history,   
        run_config=run_config, 
    ) # Returns a `RunResultStreaming` that yields partial events.
    print("===RUN STARTING===")
    async for event in stream.stream_events(): # Iterates over each streaming event, You’ll handle only the ones that contain text deltas.
          if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            await reply.stream_token(event.data.delta) # For each chunk of generated text (delta), append it to the in‑place msg in the UI
    await reply.update() # Finalizes the streamed message: closes the loop and makes sure the full content is rendered.

    # Save assistant reply to history
    history.append({"role":"assistant", "content":reply.content}) # Store final output from LLM {role:assistant} in the history as well.
    cl.user_session.set("history",history) # Saves the updated history back into the user’s session storage.

    return reply