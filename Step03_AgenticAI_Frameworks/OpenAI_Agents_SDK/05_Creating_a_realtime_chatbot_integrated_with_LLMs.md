## **1. Creating Chatbot with Chainlit UI platfrom:**

First you need to create:

- i) A `uv` project.
- ii) add OpenAI_agent_SDK into your project.
- iii) Install Chainlit into your project.

As we learned in previous sections, after that follow the following steps to create chatbot.

### **Step#1: Configuration of LLMs into your project:**

- By default, the **OpenAI Agents SDK** uses OpenAI LLMs so to plug in Google Gemini or any other LLM with OpenAI_Agents_SDK, we need following configurations:

  - i) **Store your Gemini/Other API key:**
    - Create a `.env` file and write the API key there:
      ```env
          GEMNI_API_KEY=xxxxxxx
      ```
  - ii) **Load the Key in your code as follows:**

    ```py
    from dotenv import load_dotenv
    import os

    load_dotenv()
    gemini_key = os.getenv("GEMINI_API_KEY")
    ```

  - iii) **Ignore sensitive files to be pushed into github:**

    - Create `.gitignore` file.
    - Add `.env` to `.gitignore` file.

  - iv) **Instantiate an external OpenAI‑compatible client.**

    - Because Agents SDK by default support OpenAI LLMs that's why we need an external OpenAI compatible client to run other models.

      ```py
      from agents import AsyncOpenAI
      # Reference: https://ai.google.dev/gemini-api/docs/openai
      external_client = AsyncOpenAI(
          api_key=gemini_key,
          base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
      )
      ```

  - v) **Select your Gemini model:**

    ```py
    from agents import OpenAIChatCompletionsModel

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    )

    ```

  - vi) **Configure runtime settings:**

    ```python
    from agents import RunConfig

    config = RunConfig(
        model=model,
        model_provider=external_client,
        tracing_disabled=True
    )

    ```

**Note: If you have a paid OpenAI subscription, you can skip steps 4 & 5.**

### **Step#2: Create Agent into your project:**

- **Synchronous Run (Method 1):**

  ```python
  from agents import Agent, Runners
  agent = Agent(
  name="Assistant",
  instructions="You are a helpful assistant",
  model=model
  )

  result = Runner.run_sync(
  agent,
  "Hello, how are you?",
  run_config=config
  )

  print(result.final_output)

  ```

- **2.2 Asynchronous Run (Method # 2):**

  ```python
  from agents import Agent, Runner

  async def main():
      agent = Agent(
          name="Assistant",
          instructions="You only respond in haikus",
          model=model
      )

      result = await Runner.run(
          agent,
          "Hello, how are you?",
          run_config=config
      )

      print(result.final_output)
  ```

Above Was the basic code sturcture of working with the agents SDK and Itinitalitizing the LLms other then OpenAI, but below is the code written where we can easily integrate our LLMs with Chainlit UI.

### **Step#3: - Wiring Agents into Chainlit UI (Without chat session)**

Below code will not save the chat history in your current chat session.

```python
  from agents import Runner
  import chainlit as cl  # Importing the whole chainlit module.

  @cl.on_message
  async def handle_message(message:cl.Message):
      result = await Runner.run(
          input=message.content,
          run_config=config,
          starting_agent=agent
      )
      await cl.Message(content=result.final_output).send()
```

### **Step#4: Wiring Agents into Chainlit UI (With Chat session saved)**

```py
@cl.on_chat_start
async def handle_chat_history():
    cl.user_session.set("history",[]) # Set the chat session into an Array/list
    await cl.Message(content="Hello, I am Naveed Khalid's Assistant. How can I help you today?").send()  # This message will display on your chatbot.

@cl.on_message
async def handle_message(message:cl.Message):
    history=cl.user_session.get("history") # User's message first sent to the history variable set above.

    # Standard Interface [{"role":"user",content:"Hello"},{"role":"assistant", "content":"Hello, How can I help you today"}]

    history.append({"role":"user", "content":message.content}) # History variable then append user's message into history [].

    result= await Runner.run(
        input=history,   # We are giving complete history to our llm, instead of just message.content
        run_config=run_config,
        starting_agent=agent1
    )
    history.append({"role":"assistant", "content":result.final_output}) # Store final output from LLM {role:assistant} in the history as well.

    cl.user_session.set("history",history)
    await cl.Message(content=result.final_output).send()
```

### **Important Notes:**

- Python ≥ 3.9 is required.
- Always activate your virtual environment before installing.
- Use -w for hot reload during development.
- Secure your API keys in a .env file and never commit them.
