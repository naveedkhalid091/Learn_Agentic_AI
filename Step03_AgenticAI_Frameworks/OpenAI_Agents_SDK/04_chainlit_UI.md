## Chainlit

Chainlit is an open‑source Python framework designed to help developers build, deploy and monitor production‑ready conversational UI applications in minutes rather than weeks.

Chainlit provides a rich, customizable conversation UI—but it’s more than just a front‑end widget. Chainlit is a full‑stack framework that wires your Python (or TypeScript) code to a production‑ready chat interface, handling everything from UI rendering to persistence, authentication, and monitoring.

Official Documentation - [ChainLit](https://docs.chainlit.io/get-started/overview).

### 1. Installation:

Create your project using UV as we have learnt to create the project in previous section after that you can install Chainlit as follows:

```bash
uv add chainlit
```

Note: Chainlit requires python>=3.9
This will make the chainlit command available on your system.

Make sure everything runs smoothly:

```bash
uv run chainlit hello
```

This should spawn the chainlit UI and ask for your name: Chainlit would run at http://localhost:8000 after above command.

### Step 1: Create a Python file:

- Create a file `chatbot.py` inside the src/projectname.
- This file will contain the main logic for your LLM application.

### Step 2: Write the Application Logic

- In `chatbot.py`, import the Chainlit package and define a function that will handle incoming messages from the chatbot UI. Decorate the function with the @cl.on_message decorator to ensure it gets called whenever a user inputs a message.

Here’s the basic structure of the script:

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

The main function will be called every time a user inputs a message in the chatbot UI. You can put your custom logic within the function to process the user’s input, such as analyzing the text, calling an API, or computing a result.

The Message class is responsible for sending a reply back to the user. In this example, we simply send a message containing the user’s input.

### Step 3: Activate your virtual environment

```bash
uv venv # this will show you a path/command to activate the virtual env.
```

### Step 4: Run the Application:

To start your Chainlit app, open a terminal and navigate to the directory containing `chatbot.py`. Then run the following command:

```bash
uv run chainlit run chatbot.py -w
```

Note: The -w parameter enables hot reloading when we change our code.

Now, After that Whatever you will write in chatbot, it will show you a message as per the logic written in `chatbot.py` file. For Exmaple, as per the above code, when you will write Cool, A chatbot will display `Received: Cool`.

It means that your code is working perfectly fine.
