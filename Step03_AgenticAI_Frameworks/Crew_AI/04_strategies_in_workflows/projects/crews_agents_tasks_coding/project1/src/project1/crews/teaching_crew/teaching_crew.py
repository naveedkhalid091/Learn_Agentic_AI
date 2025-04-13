from crewai import Agent, Task, Crew, Process
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TeachingCrew: # We are creating a crew named `TeachingCrew`
    # 1. Define the agents    
    def sir_naveed(self) -> Agent:
        logger.info("Creating Sir Naveed Agent")
        return Agent(
            role="Sir Naveed",
            goal="You are a teacher who is teaching a topic to a student",
            backstory="You are a Softwere Engineer(SWE). You will be teaching a topic to students",
            llm="gemini/gemini-1.5-flash",
            verbose=True
            ) # This is the configuration for the agent

    # 2. Define the tasks
    def describe_topic(self) -> Task:
        logger.info("Creating Describe Topic Task")
        return Task(
             description= "Describe the {topic} in detail. Provide a comprehensive overview of the topic. Use examples and real-world applications to illustrate the concepts.",
             expected_output="A detailed description of {topic} wich clear sections covering basics.",
             agent=self.sir_naveed(),
             verbose=True
             ) # This is the configuration for the task
        
   # 3. define the crew
    def crew(self) -> Crew:
        logger.info("Creating the crew with agents and tasks")
        return Crew(
            agents=[self.sir_naveed()], 
            tasks=[self.describe_topic()], 
            process=Process.sequential,
            verbose=True,
        )
    
       

