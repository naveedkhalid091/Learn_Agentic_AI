from crewai.flow import Flow, listen, start 
from litellm import completion


class litellmFlow(Flow):
    @start()
    def start_flow(self):
        output = completion(
            model="gemini/gemini-2.0-flash",
            messages=[
                {"role": "user", "content": "How is the founder of Pakistan?"}
            ]
        )
        return output["choices"][0]["message"]["content"]
    
def run_flow():
    obj=litellmFlow()
    result=obj.kickoff()
    print(result)

    
    
