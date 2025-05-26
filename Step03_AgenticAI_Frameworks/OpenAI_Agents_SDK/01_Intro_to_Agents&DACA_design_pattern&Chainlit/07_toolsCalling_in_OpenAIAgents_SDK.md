## Tools:

The OpenAI Agents SDK provides a robust framework for integrating various tools into agents, enabling them to perform tasks such as data retrieval, web searches, and code execution. Here's an overview of the key points regarding tool integration:

### Types of Tools:

1. **Hosted Tools:** These are pre-built tools running on OpenAI's servers alongside the AI models, accessible via the `[OpenAIResponsesModel]`. Examples include:

   - **WebSearchTool:** Enables agents to perform web searches.
   - **FileSearchTool:** Allows retrieval of information from OpenAI Vector Stores.
   - **ComputerTool:** Facilitates automation of computer-based tasks.

2. **Function Calling:** This feature allows agents to utilize any Python function as a tool, enhancing their versatility.
3. **Agents as Tools:** Agents can employ other agents as tools, enabling hierarchical task management without transferring control.

### Implementing Tools:

- **Function Tools:** By decorating Python functions with @function_tool, they can be seamlessly integrated as tools for agents.

### Tool Execution Flow:

- During an agent's operation, if a tool call is identified in the response, the SDK processes the tool call, appends the tool's response to the message history, and continues the loop until a final output is produced.

### Error Handling:

The SDK offers mechanisms to handle errors gracefully, allowing agents to recover from tool-related issues and continue their tasks effectively.

For a comprehensive understanding and implementation details, refer to the [tools documentation](https://github.com/openai/openai-agents-python/blob/main/docs/tools.md) along with coding examples.

## **Emerging Features in LLMs for Next-Level AI Agent Development:**

Function calling (often referred to as tool calling) in large language models (LLMs) is indeed a powerful feature, enabling AI agents to interact with external systems, execute tasks, and extend their capabilities beyond mere text generation. This capability has become a cornerstone for AI agent development, allowing LLMs to perform structured actions like querying databases, making API calls, or controlling devices. However, the landscape of AI agent development is rapidly evolving, and several upcoming or emerging features and trends are poised to further enhance this domain. Below, I’ll outline some of these advancements with a focus on their relevance to AI agent development.

1. **Enhanced Reasoning and Planning Capabilities:**

One of the most promising areas for AI agent development is improving LLMs' ability to reason and plan autonomously. Current function calling allows agents to execute predefined tools, but future enhancements may enable LLMs to dynamically determine when and how to use tools during a reasoning process. For example:

- **Dynamic Tool Invocation During Reasoning:** Imagine an LLM that pauses its reasoning, identifies a need for external data, calls a tool (e.g., a web search or calculator), integrates the result, and continues reasoning—all without explicit prompting. This would make agents more proactive and adaptive, key traits for complex task execution.

- **Multi-Step Planning:** Advances in models like OpenAI’s o1 series suggest that LLMs could break down complex goals into detailed, actionable steps, orchestrating multiple tool calls in sequence. This is critical for agents handling workflows like booking travel or managing inventory.

2. **Memory Management and Contextual Persistence:**

Effective AI agents need to remember past interactions and maintain context over long tasks. Upcoming features in this area include:

- **Long-Term Memory:** Beyond short-term context windows, LLMs are being developed with persistent memory systems (e.g., vector databases or episodic memory modules) that allow agents to recall relevant past actions, user preferences, or environmental states. This is vital for agents performing ongoing tasks like customer support or project management.
- **Memory Synthesis:** Some research points to agents synthesizing high-level insights from past interactions (e.g., summarizing a user’s behavior), enabling more personalized and efficient decision-making.

3. **Integration with External Systems (Beyond APIs)**
   While function calling currently focuses on API interactions, future developments could expand this:

- **Direct Environment Interaction:** Agents might interface with physical systems (e.g., IoT devices) or digital platforms (e.g., GUIs) without relying solely on APIs. For example, Large Action Models (LAMs) are emerging as an evolution of LLMs, capable of executing tasks by interpreting and acting on real-world interfaces.
- **Autonomous Tool Creation:** Instead of relying on predefined tools, LLMs could generate custom functions or scripts on the fly, tailored to specific tasks, enhancing flexibility in agent development.

4. **Guardrails and Safety Mechanisms:**

As agents become more autonomous, ensuring safe and ethical behavior is crucial. Upcoming features might include:

- **Built-In Guardrails:** LLMs could come with native constraints to prevent harmful actions, such as rejecting unethical tool calls or verifying outputs against safety criteria. This is particularly relevant for enterprise-grade agents.
- **Tracing and Explainability:** Enhanced tracing (e.g., logging an agent’s decision-making process) will allow developers to debug and refine agent behavior, making them more reliable for critical applications.

## **Coding Example of function calling tools (type#2):**

You can call function tools in OpenAI_agents_SDK by importing & using `funtion_tool` as follows:

```python
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
```
