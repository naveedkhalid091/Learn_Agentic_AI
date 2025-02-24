## Router Implementation.

As we are aware about the router workflow after reading the `00(a)_intro.md` file, now we will understand how to implement the router into code.

**Note: All steps of project initialization are same as we discussed in the Propmt chaining section but here we will adjust the schema a little bit by incoporating the `router()`.**

Below is a sample schema code that need to be adjusted and we will first import the route along with other decorators:

```python
from crewai.flow.flow import Flow, start, listen, router
import random   # import it if you want to use something randomly
# Step - 2: Below is the workflow schema code
class RouteFlow(Flow):

    @start() # step 3
    def greeting(self):
        print("Asalam-O-Alikum")

    @router(greeting) # step 3
    def select_city(self):
        cities=["lahore", "karachi", "bahawalpur", "islamabaad"]
        selected_city = random.choice(cities)
        self.state['city'] = selected_city  # return & save the selected city in state and

        if selected_city=="lahore":
            return  'lahore'
        elif selected_city=="karachi":
            return 'karachi'
        elif selected_city=="bahawalpur":
            return 'bahawalpur'
        elif selected_city=="islamabaad":
            return 'islamabaad'

    @listen("lahore")
    def city1(self):
        print(f'''Write fun facts about {self.state['city']} city''')

    @listen("karachi")
    def city2(self):
        print(f'''Write fun facts about {self.state['city']} city''')

    @listen("bahawalpur")
    def city3(self):
        print(f'''Write fun facts about {self.state['city']} city''')

    @listen("islamabaad")
    def city4(self):
        print(f'''Write fun facts about {self.state['city']} city''')


# step 4 : Kickoff the function
def execute_1():
    obj= RouteFlow()
    obj.kickoff()

def execute_2():
    obj= RouteFlow()
    obj.plot()   # this will create a plot or flowchart in .html file.

```

**Configure the Command:**

a) Update pyproject.toml

Under [project.scripts], add a script variable for your prompt chaining function:

```toml
[project.scripts]
third_chain = "prompt_chaining.main2:execute_1"
third_chain_plot = "prompt_chaining.main2:execute_2"
```

**Run the Script:**

Run your prompt chaining script via:

```bash
  uv run third_chain  # This is custom made command in toml file
```

**See the plot of your script using below:**

Run your prompt chaining script via:

```bash
  uv run third_chain_plot  # This is custom made command in toml file
```
