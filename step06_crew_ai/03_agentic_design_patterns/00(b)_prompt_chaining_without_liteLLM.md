## Workflows: Prompt Chaining (with & without liteLLM):

This guide explains how to set up and run a Prompt Chaining project without using liteLLM, along with integrating crewAI for chaining functions. Follow the steps below for a smooth setup.

### 1. **Without LiteLLM**

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

## 2. Workflows:Prompt Chaining (with liteLLM):

**Steps to start the `WorkFlow:Prompt-chaining` project.**

a) Write below command in the terminal path where you wanted to start your package.

```bash
uv init --package projectName
```

b) Navigate to the project directory created at above step.
c) Add creawai & liteLLM as dependency using `uv` manager as follows.

```bash
uv add creawai
uv add liteLLM
```

d) Create any file inside the `src` folder and write a function e.g Hello world.
e) Write a script variable i.e. `start="projectPath:functionName"` inside `pyproject.toml` under the [project.scripts] to run the script created as a function at above step.
d) Run the above created script using below command in the terminal.

```bash
uv run start
```

**NOTE: Above was the basic setup discussion without crewai, and above commands will be common in all types of projects, Now we move forward with crewai and liteLLM related project code**

e) After the above steps, now ensure the Python interpreter is set to the same environment where crewAI is installed. Open the Command Palette `(Ctrl+Shift+P or Cmd+Shift+P)` and choose `“Python: Select Interpreter”` to confirm you’re using the right environment.

f) Import the following decorators & liteLLM from the crewAI to start `prompt-chaning` as follows.

```python
from crewai.flow.flow import Flow , start , listen
from litellm import completion
```

g) Connect the LiteLLM with crewAI after generating the LLM key.

- You can connect the LLM by creating `.env` file and pasting your secret code there.

h) Write the schema code as follows and we have two to three methods to write the schema code.

- The first method is to write the schema and update the values using state like we used this concept in React. (This method is included in below code). This method is recommended becasue we can use the values generated through State method in the all upcomming functions.

- The second method is, whenever the first function `return a value` then we can use that value in the next function as in input. If you will return value through this `return` key word then you can only use the returnd value in one upcoming function only.

i) Write the Schema Code: (Below is a code which is copied from the project- fun fact)

```python
# 1. Define a class
class CityFunFact(Flow):
     # Define a starting function (first chaining function) which will at start generate title/content from the LLMs first.
     @start()
     def get_city(self):
          result=completion(
               model="gemini/gemini-1.5-flash",
               api_key=API_KEY,
               messages=[
                    {"role":"user","content":"Write a random city name from Pakistan?"}
               ]
          )
          city = result['choices'][0]['message']['content']
          print(city)
          return city   # First Method of returning

     # Define another chaining functions which will generate content from the LLMs based on the above generated content.

     @listen(get_city)
     def generate_fun_fact(self,city_name):
          result=completion(
               model="gemini/gemini-2.0-flash-exp",
               api_key=API_KEY,
               messages=[
                    {"role":"user",
                     "content":f"Tell me a fun fact about {city_name}"
                    }
               ]
          )
          fun_facts= result['choices'][0]['message']['content']
          print(fun_facts)
          self.state['fun_facts']=fun_facts  # Second Method of returning

    # Define another chaining functions which will save the generated content from the LLMs based on the above functions.

     @listen(generate_fun_fact)
     def save_fun_fact(self):
          with open("fun_facts.md", "w") as file:  # This will save the .md file in your project
                file.write(self.state['fun_facts'])  # This will write the fun fact in the file.
                print("Fun Fact Saved Successfully")
                return self.state['fun_facts'] # This is the third method of returning the value.
```
