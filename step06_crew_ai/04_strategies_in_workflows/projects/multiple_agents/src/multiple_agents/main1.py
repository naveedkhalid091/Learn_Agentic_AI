from crewai.flow import Flow, start, listen
from multiple_agents.crews.dev_crew.dev_crew import DevCrew

class DevFlow(Flow):

    @start()
    def run_dev_crew(self):
        output=DevCrew().crew().kickoff(
            inputs={
                "problem":"Write python code for addition two numbers"
            }
        )
        return output

def multiagent():
    dev_flow= DevFlow()
    result=dev_flow.kickoff()
    print(result)