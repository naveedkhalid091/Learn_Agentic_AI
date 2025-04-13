## 1. Project Initialization (with two strategies) and Environment Setup:

**a) Create a New Project**

- Initiate a new `uv` project with the following command:

```bash
uv init --package project1
```

**b) Set Up Environment Variables**

- In the project1 folder, create a file named .env.
- Add your LLM API key and model name:

```bash
GEMINI_API_KEY=your_gemini_api_key
MODEL=gemini/gemini-1.5-flash
```

**c) Project Structure and Dependencies**

- Navigate to the `src/project1` folder and create a file called `main.py`.
- Add required dependencies by running:

```bash
 uv add crewai crewai-tools
```

- **Note:** Since liteLLM is already built into crewai, you do not need to install it separately.
- If you face an import error with `crewai.flow.flow`, select the correct **Python interpreter** using `Ctrl+Shift+P → Python: Select Interpreter`.

### **2. Implementing Strategy 1: Generate a Trending Topic Using litellm**

- a) Write the Code in `main.py`
  - Insert the following code to create a flow that generates a trending topic:

```python
from crewai.flow.flow import Flow, start, listen
from litellm import completion
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())  # load the environment variables from the .env file.
model_name = os.getenv("MODEL")  # get the model name from the environment variables.
model_key = os.getenv("GEMINI_API_KEY")  # get the model key from the environment variables.

class PanaAgent(Flow):  # encapsulate the flow of the agent
    @start()
    def select_top_trending_topics(self):
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
```

- **b) Testing Strategy # 1**

  - Add a function in main.py to start the flow:

    ```python
      def start_flow():
        flow=PanaAgent()
      flow.kickoff()
    ```

  - Configure your project’s .toml file (under the script section) with:

  ```bash
    #For Example
    panaflow = "project1.main:start_flow"
  ```

  - Run the project using:

```bash
uv run panaflow
```

**Note:** This will execute the code and print the selected trending topic.

### 3) **Implementing Strategy 2: Create a Crew with crewai:**

- a) **Set Up the Crew Directory:**
  - Inside your project folder (`project1` under `src`), create a new folder called `crews`.
  - Within `crews`, create another folder named `teaching_crew` (naming the crew based on its purpose).
  - In the `teaching_crew` folder, create a file called `teaching_crew.py`
  -
- b) **Write the Crew Code in `teaching_crew.py`.**

  - Insert the following code to define a teaching crew with its agents and tasks:

  ```python
  from crewai import Agent, Task, Crew, Process
  import logging

  logging.basicConfig(level=logging.INFO)
  logger = logging.getLogger(**name**)

  class TeachingCrew: # We are creating a crew named `TeachingCrew` # 1. Define the agents
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

  # 3. Define the crew

    def crew(self) -> Crew:
      logger.info("Creating the crew with agents and tasks")
        return Crew(
          agents=[self.sir_naveed()],
          tasks=[self.describe_topic()],
          process=Process.sequential,
          verbose=True,
        )
  ```

  c) **Integrate the Crew with Your Main Flow in `main.py`**

  - Update `main.py` to import and use the teaching crew:

  ```python
  from crewai.flow.flow import Flow, start, listen
  from litellm import completion
  from dotenv import load_dotenv, find_dotenv
  import os
  from project1.crews.teaching_crew.teaching_crew import TeachingCrew
  import logging

  load_dotenv(find_dotenv()) # load the environment variables from the .env file.
  model_name = os.getenv("MODEL") # get the model name from the environment variables.
  model_key = os.getenv("GEMINI_API_KEY") # get the model key from the environment variables.

  class PanaAgent(Flow): # encapsulates the flow of the agent

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
  ```

- The above integration will first generate a trending topic and then pass it to the teaching crew, which will describe the topic in detail.
