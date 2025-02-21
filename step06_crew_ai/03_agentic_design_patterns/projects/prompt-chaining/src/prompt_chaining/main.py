# Implementing the Basic Flow with Prompt Chaining: 
from crewai.flow.flow import Flow , start , listen   # import the Flow, start and listen from crewAI.
from litellm import completion    # Import the completion from LiteLLM.

import time                        # import the time module to use the sleep function.

## 1. Basic Function or package without crewAI and LiteLLM
def function1():
    print("Hello World")

## 2. Below is the code with crewAI but without LiteLLM. 
class SimpleFlow(Flow):

        @start()    # Indicates the starting function/tool.
        def function1(self):
            print("step1...!")
            time.sleep(3)   # This is just to show that the function will run afer 3 seconds of start.

        @listen(function1)   # Wait for the function1 to finish and then start this function.
        def function2(self):
            print("step2...!")
            time.sleep(3)   # This is just to show that the function will run afer 3 seconds of function1.

        @listen(function2)   # Wait for the function2 to finish and then start this function.
        def function3(self):
            print("step3...!")
            time.sleep(3)  # This is just to show that the function will run afer 3 seconds of function2.


def chain():
    obj=SimpleFlow()
    obj.kickoff()  ## Where kickoff is the inherent method is Flow parameter which we placed in SimplFlow()


# 3. Below is the Code with both crewAI & LiteLLM .
        # First of all we will connect the LiteLLM with crewAI after copying the LLM key.
        # After that we will write the schema code.
        # We have two to three methods to write the schema code. 
        # 1) The first method is to write the schema and update the values using State like we used this concept in React.
        # 2) The second method is, whenever the first function `return a value` then we can use that value in the next function as in input.  
        
        

API_KEY="AIzaSyAdFjAY6i961XHdC1VX9yT_IPEYKVwJS38"
class CityFunFact(Flow):
     # Below function will generate a random city name from Pakistan.
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
          return city   # First Method of returning values
     
     # Below function will generate a fun fact about the city.
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
          self.state['fun_facts']=fun_facts  # Second Method of returning  values instead of `return` key word - This method recommended
    
    # Below function will save the fun fact in the file.  
     @listen(generate_fun_fact)
     def save_fun_fact(self):
          with open("fun_facts.md", "w") as file:  # This will save the .md file in your project 
                file.write(self.state['fun_facts'])  # This will write the fun fact in the file.
                print("Fun Fact Saved Successfully")
                return self.state['fun_facts'] # This is the third method of returning the value.
    

# Below is the function which will call the above schema code.
def city_name():
     obj=CityFunFact()
     result = obj.kickoff()
     print(result)
