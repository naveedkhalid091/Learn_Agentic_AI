from crewai import Agent, Crew, Task, LLM
from crewai.tools import BaseTool  # import it if you wanted to create tool using method # 1
from pydantic import BaseModel, Field # import it if you wanted to create tool using method # 1
from typing import Type  # import it if you wanted to create tool using method # 1
from crewai.tools import tool   # import it if you wanted to create tool using method # 2
import os

# from dotenv import load_dotenv
# load_dotenv()

# Setup API Keys & MODEL

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
SERPER_API_KEY=os.getenv("SERPER_API_KEY")
MODEL=os.getenv("MODEL")

## llm 
llm1=LLM(model="gemini/gemini-2.0-flash")

# embedder_config

embedder_config ={
    "provider":"google",
    "config":{
        "model":"models/text-embedding-004",
        "api-key":os.getenv("GEMINI_API_KEY")
        }
 }

# 1. Create Tool using OOP method

# Define input structure through pydantic schema below:
class MyToolInput(BaseModel):
    """Input Schema for MyCustomTool """
    stu_name:str = Field(...,description="Student Name")
    stu_roll_no:int = Field(..., description="student id")

# Create a class and extend it with the BaseTool
class PiaicStudentCard(BaseTool):
    # tool name
    name : str = "PIAIC Student Card Generator"
    # What should the tool perform, write in description below:
    description:str= " this function will create PIAIC student card of registered students."
    # Write the paramters, which your tool will take.
    args_schema:Type[BaseModel]=MyToolInput

# Finally, when user will provide name and roll numbers then _run function defined below will return a card with below content.

    def _run(self, stu_name:str , stu_roll_no:int)-> str:
        # your tool's logic here
        return f""" PIAIC Student Card
        student name : {stu_name}
        student roll no : {stu_roll_no}
        """
#2. Create another tool using method 2: 

@tool("PIAIC fee update") # this tool decorator will configure all the things automatically which we have done in the first method.
def my_tool(roll_no:int)->dict|str:  # write a simple function which will now considered a tool automatically because of tool().
    """ this function will search piaic student fee updates, it will require roll number of PIAIC student"""
    #database
    data={100,"paid",
    200,"upaid"
    }

    status= data.get(roll_no)
    if status:
        return {"status":status}
    else:
        return "student not found"

# Create an object of your custom tools "PiaicStudentCard" & "my_tool": 

card=PiaicStudentCard()

piaic_manager=Agent(
    role="PIAIC Manger",
    goal="Manage all queries regarding PIAIC and you will use only relevent tools for student query",
    backstory="You are master at understanding people and thier preferences",
    tools=[card,my_tool],
    llm=llm1,
    verbose=True,
)

piaic_card_creator=Task(
    description="You will be responsbile for all piaic relevent operations, student query '{query}', you must know how to answer his question based on the data you have fetched or taken from Agent.",
    expected_output="Only respond based on the user's query.",
    agent=piaic_manager
)

crew=Crew(
agents=[piaic_manager],
tasks=[piaic_card_creator],
verbose=True
)

def my_card():  
    result=crew.kickoff(
        inputs={"query":"I am PIAIC student my name is Naveed Khalid and my roll number is 100. Please create my student card and check if my fee is paid?"}
    )
    print(result)


