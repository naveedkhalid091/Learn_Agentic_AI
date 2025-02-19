## Workflows coding

i) We will first write example code of `prompt_chaining`,

**Steps to start the Prompt-chaining project.**

a) Write below command in the terminal path where you wanted to start your package.

```bash
uv init --package projectName
```

b) Navigate to the project directory created at above step.
c) Add creawai as dependency using `uv` manager as follows.

```bash
uv add creawai
```

d) Create any file inside the `src` folder and write a function e.g Hello world.
e) Write a script variable i.e. `start="projectPath:functionName"` inside `pyproject.toml` under the [project.scripts] to run the script created as a function at above step.
d) Run the above created script using below command in the terminal.

```bash
uv run start
```

e) Ensure the Python interpreter is set to the same environment where crewAI is installed. Open the Command Palette `(Ctrl+Shift+P or Cmd+Shift+P)` and choose `“Python: Select Interpreter”` to confirm you’re using the right environment.

f) Import the following decorators from the crewAI to start prompt-chaning as follows.

```python
from crewai.flow.flow import Flow , start , listen
```

g) Create a Class first and inside this class you can start chaining as follows:

```python
    from crewai.flow.flow import Flow , start , listen`

     class SimpleFlow()`
```

h) Extend the above `SimpleFlow` class by placing the class `Flow` as parameter, this has made all the functions/features available of Flow class.

Coding is mentioned below:

```python
    from crewai.flow.flow import Flow , start , listen`

     class SimpleFlow(Flow):
```

i) Create the functions inside the `SimpleFlow` class as follows:

```python
    from crewai.flow.flow import Flow , start , listen`

     class SimpleFlow(Flow):

        def function1(self):
            print("step1...!")

        def function1(self):
            print("step2...!")

        def function1(self):
            print("step3...!")
```

j) Write decorator functions `start` & `Listen` before any function. `Start` decorator function will indicate where to start the flow and `listen` indicates which function to start after mentioning the prvious function as follow.

```python
    from crewai.flow.flow import Flow , start , listen`

     class SimpleFlow(Flow):

        @start()    # Indicates the starting function/tool.
        def function1(self):
            print("step1...!")

        @listen(function1)   # Wait for the function1 to finish and then start this function.
        def function2(self):
            print("step2...!")

        @listen(function2)   # Wait for the function2 to finish and then start this function.
        def function3(self):
            print("step3...!")
```

k) Now you have defined the chain of functions, the next step is to call all of these functions simoultaneously by making an object/variable and placing above class into an object/variable as follows.

```python

def chain():

    obj=SimpleFlow()

    obj.kickoff()  ## where kickoff is the inherent method is Flow parameter which we placed in SimplFlow()

```

l) Write a script variable of prompt chaining i.e. `first_chain="prompt_chaining.main:chain"` inside `pyproject.toml` under the [project.scripts] to run the script created as a function at above step.

d) Run the above created script using below command in the terminal.

```bash
uv run first_chain
```
