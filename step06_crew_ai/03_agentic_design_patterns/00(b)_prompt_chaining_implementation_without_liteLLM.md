## Workflows: Prompt Chaining (with & without liteLLM):

This guide explains how to set up and run a Prompt Chaining project without using liteLLM, along with integrating crewAI for chaining functions. Follow the steps below for a smooth setup.

The summary in steps is mentioned below:

**Step 1- Install project & Import Required Decorators:** After setting up your uv project and adding dependencies (crewai and liteLLM), start by importing the Flow, start, and listen decorators.
**Step 2- Create the Workflow Schema:** Create a class that defines your workflow. Inside this class, write separate functions for each step of your prompt chain.
**Step 3- Link the Functions:** Use the start and listen decorators to link these functions together in the order you want them to run.
**Step 4- Kick Off the Workflow:** Trigger the workflow with the kickoff method to run your defined sequence of prompts.
**Step 5- Configure the Command:** Set up a script variable in your `pyproject.toml` file (under [project.scripts]) that points to your workflow function. This ensures the correct command is configured to run your prompt chain.
**Step 6- Run the Script:** Finally, execute your configured command (for example, using uv run your_script_name) to see your prompt chain in action.

Now lets understand above steps through coding examples:

**Basic Project Setup**

1. **Initialize the Project Package:**
   - Open a terminal in the desired directory and run:

```bash
   uv init --package projectName
```

2. **Navigate to the Project Directory:**

   - Change to the newly created project directory:

```bash
  cd projectName
```

3. **Add the creawai Dependency:**

   - Install the dependency using the uv package manager:

```bash
uv add creawai
```

4. **Create a Python File:**

   - Inside the `src` folder, create a file (e.g., `main.py`) and write a simple function (for example, a "Hello World" function).

5. **Configure Script in `pyproject.toml`**

   - Under the [project.scripts] section, add a script variable that points to your function:

```toml
[project.scripts]
start = "projectPath:functionName"
```

6. **Run the Script**

- Execute the script using:

```bash
uv run start
```

**Note: The above steps cover the basic setup without crewAI. The following sections detail how to integrate crewAI for prompt chaining.**

Integrating crewAI for Prompt Chaining

a) Verify Your Python Interpreter:

- Ensure that the Python interpreter is set to the environment where crewAI is installed.
- Open the Command Palette `(Ctrl+Shift+P or Cmd+Shift+P)` in your editor and select Python: Select Interpreter.

b) Import crewAI Decorators:

- In your Python file, import the necessary decorators from crewAI:

  ```python
  from crewai.flow.flow import Flow, start, listen
  ```

c) Define the Prompt Chaining Schema:

1. Create the Base Class:

   - Create a class (e.g., SimpleFlow) to define your prompt chaining schema:

   ```python
   from crewai.flow.flow import Flow, start, listen
   class SimpleFlow():
   ```

2. Extend the Class from Flow:

   - Inherit from the Flow class to gain all its functionalities:

   ```python

    from crewai.flow.flow import Flow, start, listen

    class SimpleFlow(Flow):


   ```

3. Define Functions in the Class:

   - Add the functions that represent each step in your prompt chaining process:

   ```python
   from crewai.flow.flow import Flow, start, listen

    class SimpleFlow(Flow):

        def function1(self):
            print("step1...!")

        def function2(self):
            print("step2...!")

        def function3(self):
            print("step3...!")
   ```

4. Apply the crewAI Decorators

- Use the @start() decorator to indicate the starting point, and @listen() to define subsequent steps:

```python

from crewai.flow.flow import Flow, start, listen

 class SimpleFlow(Flow):

 @start()    # Starting function/tool.
 def function1(self):
     print("step1...!")

 @listen(function1)   # Wait for function1 to finish before executing.
 def function2(self):
     print("step2...!")

 @listen(function2)   # Wait for function2 to finish before executing.
 def function3(self):
     print("step3...!")
```

d) Kick Off the Flow:

Create a function to instantiate your class and trigger the chained functions using the inherent kickoff method:

```python
def chain():
    obj = SimpleFlow()
    obj.kickoff()  # kickoff method is provided by Flow
```

e) Configure and Run the Prompt Chaining Script:

1. Update pyproject.toml

   - Under [project.scripts], add a script variable for your prompt chaining function:

   ```python
   [project.scripts]
   first_chain = "prompt_chaining.main:chain"
   ```

2. Execute the Script:
   Run your prompt chaining script via:

```bash
  uv run first_chain
```
