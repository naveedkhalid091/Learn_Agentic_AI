## Workflows: Prompt Chaining (with liteLLM):

This guide explains how to set up and run a Prompt Chaining project using crewAI in combination with liteLLM. Follow the steps below to create your project, install the required dependencies, and write your prompt-chaining schema.

1. **Basic Project Setup:**

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

   Inside the `src` folder, create a Python file (for example, main.py) and write a simple function (e.g., a "Hello World" function).

   **e) Configure the Script:**

   In your pyproject.toml file under the [project.scripts] section, add a script variable that points to your function:

   ```python
   [project.scripts]
   start = "projectPath:functionName"
   ```

   **f) Run the Script:**

   Execute the script using the following command:

   ```bash
   uv run start
   ```

   **Note: The above steps cover the basic project setup without crewAI integration. The commands here are common to all projects. Next, we will integrate crewAI and liteLLM into the project.**

#### **2. Integrating crewAI and liteLLM for Prompt Chaining:**

**a) Set Up the Python Interpreter:**

Ensure that your Python interpreter is set to the environment where crewAI is installed. Open your editor's Command Palette (Ctrl+Shift+P or Cmd+Shift+P) and select Python: Select Interpreter to confirm the correct environment is being used.

**b) Import Required Modules:**

In your Python file, import the necessary decorators from crewAI along with the liteLLM completion function:

```python
from crewai.flow.flow import Flow, start, listen
from litellm import completion
```

**c) Connect LiteLLM with crewAI:**

After generating your LLM key, connect LiteLLM by creating a `.env` file in your project directory and pasting your secret API key into it.

**d) Writing the Prompt-Chaining Schema:**

There are multiple methods to pass data between chained functions:

- **Method 1:** Using State:
  Update values in a shared state (similar to React state) to use in subsequent functions. This method is recommended as it allows the generated values to be accessed in all upcoming functions.

- **Method 2:** Using Return Values
  Return a value from a function to be used as input for the next function. Note that the returned value is only available to the immediate next function.

Below is a sample schema code demonstrating the first & second methods

```python

# 1. Define a class inheriting from Flow
class CityFunFact(Flow):

    # Starting function: generates a city name using an LLM.
    @start()
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
    @listen(get_city)
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
    @listen(generate_fun_fact)
    def save_fun_fact(self):
        with open("fun_facts.md", "w") as file:
            file.write(self.state['fun_facts'])  # Write the fun fact to file
        print("Fun Fact Saved Successfully")
        return self.state['fun_facts']  # Third method of returning a value
```
