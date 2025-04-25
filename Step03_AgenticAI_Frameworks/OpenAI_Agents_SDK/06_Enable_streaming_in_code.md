## Streaming:

Streaming means getting data bit by bit over the time, not waiting for everything at once.

To Enable streaming in your project, you need to write following code into your project.

```python
import chainlit as cl
from dotenv import load_dotenv, find_dotenv
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig
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


# Step 4: Create your Agent

    # Method # 1 (Agent method -run level) of calling LLm from chainlit.

agent1=Agent(name="Panaversity Support Agent",
            instructions="You are a helpful assistant, can answer the questions ",
            model=model
            )

# Step #5 : Integration of your above defined model and configuration with Chainlit for UI:


# i) Initialitizing an empty list of history
@cl.on_chat_start
async def handle_chat_history():
    cl.user_session.set("history",[]) # setting the empty list With its key `history`, using this key user can track the history of chat in current session.
    await cl.Message(content="Hello, I am Naveed Khalid's Assistant. How can I help you today?").send() # Send a one time welcome message at UI.

@cl.on_message
async def handle_message(message:cl.Message):
    # Retrieve history and append user message
    history=cl.user_session.get("history")
    history.append({"role":"user", "content":message.content})
    cl.user_session.set("history",history)

    # Send a placeholder for streaming reply
    reply= cl.Message(content="My Response is Generated below:\n \n")
    await reply.send()

    # Run the agent with streaming

    stream= Runner.run_streamed(
        starting_agent=agent1,
        input=history,
        run_config=run_config,
    ) # Returns a `RunResultStreaming` that yields partial events.
    async for event in stream.stream_events(): # Iterates over each streaming event, You’ll handle only the ones that contain text deltas.
          if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            await reply.stream_token(event.data.delta) # For each chunk of generated text (delta), append it to the in‑place msg in the UI
    await reply.update() # Finalizes the streamed message: closes the loop and makes sure the full content is rendered.

    # Save assistant reply to history
    history.append({"role":"assistant", "content":reply.content}) # Store final output from LLM {role:assistant} in the history as well.
    cl.user_session.set("history",history) # Saves the updated history back into the user’s session storage.

    return reply

```

and finally start the Chainlit UI in your **Localhost:8000** through following command:

```bash
uv run chainlit run chatbot.py -w  # where `chatbot.py` is the file name where your code is written
```

**Note: only two following changes are shown in above code to enable the streaming, all other code is approximately same as we have learned in previous sections:**

1. `Runner.run_streamed()` Function :
   - When we use `Runner.run_streamed()` from OpenAI Agents, it starts sending events over time, like pieces of a puzzle arriving one by one.
2. Run the Loop `async for event in result.stream_events():`
   - The loop `async for event in result.stream_events():` is like a bucket that catches each piece as it comes, allowing you to do something with it, such as printing text as it's generated or logging agent actions. Without this loop, you’d just have the stream set up but wouldn’t be able to see or use the events, missing out on real-time updates.

**Note: You can also see a project named: `hello_agent` inside the `_projects` directory, where we have created agents with history and streaming enabled.**

**Note#2: There are many types of events which we have written in code i.e `event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):`, and we will discuss these types more in detail later on.**
