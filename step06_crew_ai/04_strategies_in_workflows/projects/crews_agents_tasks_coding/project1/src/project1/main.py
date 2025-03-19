from crewai.flow.flow import Flow, start, listen
from litellm import completion
from dotenv import load_dotenv, find_dotenv
import os
from project1.crews.teaching_crew.teaching_crew import TeachingCrew
import logging


load_dotenv(find_dotenv())  # load the environment variables from the .env file.
model_name = os.getenv("MODEL")  # get the model name from the environment variables.
model_key = os.getenv("GEMINI_API_KEY")  # get the model key from the environment variables.

class PanaAgent(Flow):  # encapsulates the flow of the agent
    
    # 1. Select the trending topics
    @start()
    def generate_topic(self):
        print("Generating the topic")
        response=completion(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that selects the trending and interesting topics & You will give atleast one topic at any cost without any furthersuggestion."
                },
                {"role": "user", "content": "What are the trending topics in AI Industry? only share topic, no other content"}
            ],
            max_tokens=100,
            temperature=0.5
        )
        self.state['topic']=response['choices'][0]['message']['content']
        print(f"Step-1 : Selected Topic: {self.state['topic']}")

    # 2. Assign the topic to the crew
    @listen("generate_topic")
    def generate_content(self):
        # 1. create crew
        print("Step-2 : Generating the content")
        teaching_crew=TeachingCrew()
        crew_instance=teaching_crew.crew()
        result= crew_instance.kickoff(
            inputs={"topic":self.state['topic']}
        )
        

def start_flow():
    flow=PanaAgent()
    flow.kickoff()

