## Learn to use the litellm in the flows:

### 1. Create flow Project using below command:

```bash
crewai create flow projectName
```

Step#2: Go to `.env` file and write the LLM key & model name to connent with the LLM.
Step#3: create `main1.py` file inside the `src/projectName`
Step#4: write below code in main.py file:

```python

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

```

Step#5: Define the command in [project.scripts] to run the above created function `run_flow`

```toml
simple-llm="project_litellm.main1:run_flow"
```

**Where:**
simple-llm = Variable/object defined
project_litellm.main1 = Path of function to run
run_flow = function name in the file that need to execute.

## Learn to execute deepseek model (Chinese LLM model) into your local Machine:
