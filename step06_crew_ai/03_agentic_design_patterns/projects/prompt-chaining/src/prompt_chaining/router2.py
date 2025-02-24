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

