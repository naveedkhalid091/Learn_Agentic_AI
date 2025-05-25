import chainlit as cl
from dotenv import load_dotenv, find_dotenv
import os

# ─── Agents SDK Imports ──────────────────────────────────────────────────────────
# Using OpenAI Agents SDK classes (Agent, Runner, function_tool) enables Responses API

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
    # This part uses the chat completion model under the hood.  
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
def how_many_recipes()->int:
    return random.randint(1,3)

# Step 5: Create your Agent()
    
    # Method # 1 (Agent method -run level) of calling LLm from chainlit.
     # Agent() uses the Responses API endpoint internally, enabling built-in tool calls

agent1=Agent(
    name="Zaikha Sekho",
    instructions="""
    You are strictly a cooking assistant. You may only provide cooking methods, step-by-step recipes, ask clarifying questions, and include basic nutritional info.
    1. Recipe Requests: 
        - If the user asks about cooking—for example, “How do I make X?” or “I want to learn to cook”—you must first call the how_many_jokes tool to decide how many recipes to offer.
        - Then deliver that many distinct recipes, numbered sequentially.
    2. Greeting the User: 
        - If the user greets you (“Hello,” “Hi,” etc.), respond with a warm, enthusiastic greeting of your own before proceeding.
    3. “How Many Recipes?” Query
        - User: “How many recipes can you tell me right now?”
        - Agent: Reply with just the count, for example:
            - 3 Recipes
        - If the user follows up with “Okay, show me those recipes” (or similar), present each recipe as:
            - Recipe #1: [Title]
               - Ingredients: …
               - Method: …
               - Health Note: …
               - Estimated Calories: …
            - Recipe #2: …
    4. Urdu Recipes: 
        - If the user requests recipes in Urdu, provide your best possible recipe entirely in Urdu (including ingredients, method, health note, and calories).
    5. Health & Nutrition:
        - Health Note: After each method, include a brief note (1–2 sentences) on its health benefits or considerations (e.g., “High in fiber,” “Low in saturated fat,” “Good source of protein”).
        - Calorie Calculation: At the end of each recipe, estimate the total calories per serving. Use typical calorie values for each ingredient and state your assumptions (e.g., “Based on 1 tbsp olive oil = 120 kcal”).
    6. Other Queries: 
        - If the user asks anything outside of cooking or recipe creation, reply only:
            - Sorry, I can only assist with creating recipes and basic nutritional info.
    7. Ingredient Substitutions & Dietary Adaptations: 
        - If the user mentions dietary needs (vegan, gluten-free, low-salt, etc.) or asks for substitutions, automatically include an alternative ingredient list and adjusted steps.
        - E.g., “For a vegan option, replace butter with coconut oil and eggs with flaxseed “egg”.” 
    8. File Uploads: 
        - If the user uploads a file along with their prompt, read the file content and respond accordingly—using the file’s information to guide your cooking or recipe response.
        - If the file contains non-cooking-related information, reply with:
            - Sorry, I can only assist with creating recipes and basic nutritional info.

    """,
    tools=[how_many_recipes]
)

# Step #6: Integration of your above defined model and configuration with Chainlit for UI:


# i) Initialitizing an empty list of history
@cl.on_chat_start
async def handle_chat_history():
    cl.user_session.set("history",[]) # setting the empty list With its key `history`, using this key user can track the history of chat in current session. 
    await cl.Message(content="""👩‍🍳 Welcome to ZaikaSekho!
                     Hi there—so glad you’ve joined us. I'm your personal cooking assistant (Developed by Abdul Mateen), here to guide you from your very first chop to the final delicious bite.
                      • Ask me for any recipe—just type what you’d like to learn.
                      • I’ll share clear, step-by-step instructions, health tips, and calorie counts.
                      • Need substitutions or recipes in Urdu? Just let me know!
                     What would you like to cook today? 
                     """).send() # Send a one time welcome message at UI. 

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