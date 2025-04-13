## Workflows: Prompt Chaining (with liteLLM):

This guide explains how to set up and run a Prompt Chaining project using crewAI in combination with liteLLM. Follow the steps below to create your project, install the required dependencies, and write your prompt-chaining schema.

The summary in steps is mentioned below:

**Step 1- Install project & Import Required Decorators:** After setting up your uv project and adding dependencies (crewai and liteLLM), start by importing the Flow, start, and listen decorators.
**Step 2- Create the Workflow Schema:** Create a class that defines your workflow. Inside this class, write separate functions for each step of your prompt chain.
**Step 3- Link the Functions:** Use the start and listen decorators to link these functions together in the order you want them to run.
**Step 4- Kick Off the Workflow:** Trigger the workflow with the kickoff method to run your defined sequence of prompts.
**Step 5- Configure the Command:** Set up a script variable in your `pyproject.toml` file (under [project.scripts]) that points to your workflow function. This ensures the correct command is configured to run your prompt chain.
**Step 6- Run the Script:** Finally, execute your configured command (for example, using uv run your_script_name) to see your prompt chain in action.

Now lets understand above steps through coding examples:

### **Step - 1 Install uv project & Import Required Decorators:**

**a) Initialize the Project Package:**
Open your terminal in the directory where you want to create your package and run:

```bash
uv init --package projectName
```

**b) Navigate to the Project Directory:**

Change to the newly created project directory:

```bash
cd projectName
```

**c) Add Dependencies:**

Add both creawai and liteLLM as dependencies using the uv package manager:

```bash
uv add creawai
uv add liteLLM
```

**d) Create a Python File:**

Inside the `src` folder, create a Python file (for example, main.py) for writting functions.

### **Step - 2 & Step - 3 Create the Workflow Schema & Link the Functions **

Below coding example represents step 2 and step 3 combined and the step 3 is mentioned in comments only as a reference because all other code is related to the step 2:

**a) Set Up the Python Interpreter:**

Ensure that your Python interpreter is set to the environment where crewAI is installed. Open your editor's Command Palette (Ctrl+Shift+P or Cmd+Shift+P) and select Python: Select Interpreter to confirm the correct environment is being used.

**b) Import Required Modules:**

In your Python file, import the necessary decorators from crewAI along with the liteLLM completion function.

```python
from crewai.flow.flow import Flow, start, listen
from litellm import completion
```

**c) Connect LiteLLM with crewAI:**

After generating your LLM key, connect LiteLLM by creating a `.env` file in your project directory and pasting your secret API key into it.

**d) Writing the Prompt-Chaining Schema:**

There are two methods to pass data between chained functions:

- **Method 1:** Using State:
  Updating values using `self.state` method to use in subsequent functions. This method is recommended as it allows the generated values to be accessed in all upcoming functions.

- **Method 2:** Using Return Values
  Return a value from a function to be used as input for the next function. Note that the returned value is only available to the immediate next function.

Below is a sample schema code demonstrating the first & second methods

```python

# 1. Define a class inheriting from Flow
class CityFunFact(Flow):

    # Starting function: generates a city name using an LLM.
    @start()  # Step 3
    def get_city(self):
        result = completion(
            model="gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[
                {"role": "user", "content": "Write a random city name from Pakistan?"}
            ]
        )
        city = result['choices'][0]['message']['content']
        print(city)
        return city   # First method of returning a value

    # Chained function: uses the generated city name to produce a fun fact.
    @listen(get_city)   # Step 3
    def generate_fun_fact(self, city_name):
        result = completion(
            model="gemini/gemini-2.0-flash-exp",
            api_key=API_KEY,
            messages=[
                {"role": "user", "content": f"Tell me a fun fact about {city_name}"}
            ]
        )
        fun_facts = result['choices'][0]['message']['content']
        print(fun_facts)
        self.state['fun_facts'] = fun_facts  # Second method of returning a value

    # Chained function: saves the generated fun fact to a Markdown file.
    @listen(generate_fun_fact)  # Step 3
    def save_fun_fact(self):
        with open("fun_facts.md", "w") as file:
            file.write(self.state['fun_facts'])  # Write the fun fact to file
        print("Fun Fact Saved Successfully")
        return self.state['fun_facts']  # Third method of returning a value
```

**Step 4- Kick Off the Workflow:**

**a) Kick Off the Flow:**

Create a function to instantiate your class and trigger the chained functions using the inherent kickoff method:

```python
def chain2():
    obj = CityFunFact()
    obj.kickoff()  # kickoff method is provided by Flow
```

**Step 5- Configure the Command:**

a) Update pyproject.toml

Under [project.scripts], add a script variable for your prompt chaining function:

```toml
[project.scripts]
second_chain = "prompt_chaining.main:chain2"
```

**Step 6- Run the Script:**

Run your prompt chaining script via:

```bash
  uv run second_chain
```
