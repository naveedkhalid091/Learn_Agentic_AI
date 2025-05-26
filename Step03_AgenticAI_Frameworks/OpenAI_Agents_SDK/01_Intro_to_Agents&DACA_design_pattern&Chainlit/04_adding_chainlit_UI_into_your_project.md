## Chainlit Overview:

Chainlit is an open-source framework that helps you create chatbots UI, very fast. It’s easy to set up, with steps like activating a virtual environment and installing it with simple commands. You can customize how the chat looks and works, and it even supports quick updates while coding. It works well with other AI tools like OpenAI or LangChain, making it flexible for different projects.

Official Docs - [ChainLit](https://docs.chainlit.io/get-started/overview).

### **1. Installation & First Run:**

You should first create your UV project and install OpenAI SDK as we have learned in previous sections and then follow below steps to continue.

i). Activate Virtual Environment.

```bash
uv venv # this will show you a path/command to activate the virtual env.
```

ii). Install Chainlit

```bash
uv add chainlit  # pip install chainlit
```

**Requires Python ≥ 3.9**

iii) Open the Chainlit UI (User Interface)

```bash
uv run chainlit hello
```

- Chainlit would run at http://localhost:8000 after above command.

### 2. Your First Chainlit App

- **2.1 Project Setup:**

  - Create a file `chatbot.py` inside the src/projectname.
  - This file will contain the main logic for your LLM application.

- **2.2 Basic APP Logic:**

  - Inside the `chatbot.py`, Write the following code:

    ```py
    import chainlit as cl

    @cl.on_message
    async def main(message: cl.Message):
        # Your custom logic goes here...

        # Send a response back to the user
        await cl.Message(
            content=f"Received: {message.content}",
        ).send()
    ```

    - @cl.on_message: decorator to handle each incoming message:

- **2.3 Running with Hot Reload:**

  - To start your Chainlit app, open a terminal and navigate to the directory containing `chatbot.py`, then run the following command:

```bash
uv run chainlit run chatbot.py -w
```

Note: The -w parameter enables hot reloading when we change our code.

Now, After that Whatever you will write in chatbot, it will show you a message as per the logic written in `chatbot.py` file. For Exmaple, as per the above code, when you will write Cool, A chatbot will display `Received: Cool`.

It means that your code is working perfectly fine.

In the Next Section we will create Chatbot with Chainlit and follow the above steps and some additional steps as well:
