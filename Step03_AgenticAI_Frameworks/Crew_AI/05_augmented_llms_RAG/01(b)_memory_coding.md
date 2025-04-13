## Memory Coding:

The Memory Coding is same as the coding which we have learned in the `knowledge.md` section but with a little bit change of below in the `main1.py` file:

- Enabling Memory
- Importing Memory & storage packages.
- Assigning the Path of storage.

The coding is mentioned below:

1. Create a Project:
   ```bash
   creawi create flow ProjectName
   ```
2. Navigate to the Project Directory
   ```bash
   cd ProjectName
   ```
3. Set Gemini keys & model into `.env` file

   ```.env
     GEMINI_API_KEY=YOUR_API_KEY
     MODEL=gemini/gemini-2.0-flash
   ```

4. Create `main1.py` file inside the `src>ProjectName` & write the following code as an example:

```python
from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
# from crewai.memory.storage import LTMSQLiteStorage, RAG Storage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage
from crewai.memory.storage.rag_storage import RAGStorage
from typing import List, Optional
import os

# Get the GEMINI API key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Define Embedder for embeddings
embedder={
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": GEMINI_API_KEY,
        }
        }
# Create a knowledge source
content = "Users name is Naveed. He is 30 years old and lives in Islamabad,Pakistan. Working as a sub-contractor at Johal & Co"

string_source = StringKnowledgeSource(
    content=content,
)

# Create an LLM with a temperature of 0 to ensure deterministic outputs
gemini_llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=GEMINI_API_KEY,
    temperature=0,
)

# Create an agent with the knowledge store
# You can also define below configuations in config folder > `agents.yaml` file
agent = Agent(
    role="About User",
    goal="You know everything about the user.",
    backstory="""You are a master at understanding people and their preferences.""",
    verbose=True,  # True means it will show all the tasks whatever agent is performing
    allow_delegation=False,
    llm=gemini_llm,
    embedder=embedder, # embedder defined in variable above
)

task = Task(
    description="Answer the following questions about the user: {question}",
    expected_output="An answer to the question.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    memory=True, # Now your crew is enabled to save all the things in its default folder storage.
    # If you want to store things into your own path then manage long term, short term & Entity memory as follows:
    # Long term management for persistent storage across sessions:
    long_term_memory=LongTermMemory(
        storage=LTMSQLiteStorage(
            db_path="./my_memory/long_term_memory_storage.db" # at this path the my_memory folder will be created to store the memory
        )

    ),
    # Short term memory for current context using RAG
    short_term_memory=ShortTermMemory(
        storage=RAGStorage(
            embedder_config=embedder, # embedder already defined as a variavle above
            type="short_term",
            path="./my_memory/short_term1/" # at this path the my_memory folder will be created to store the short term memory

        )
    ),
    entity_memory=EntityMemory(
        storage=RAGStorage(
            embedder_config=embedder,
            type="short_term",
            path="./my_memory/entity1/" # at this path the my_memory folder will be created to store the Entity memory
        )
    ),
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[string_source], # knowledge_source can be pdf,string,json etc but we are currently working with simple string
    embedder={
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": GEMINI_API_KEY,
        }
    }
)

def my_memory():
    result = crew.kickoff(inputs={"question": "What city does Naveed live in and how old is he?"})
    print(result)
```

5. Create a variable in toml file under the [project.script] to run the above project e.g.

```toml
memory="01_knowledge.main1:my_memory"
```

6. Install google generative AI as follows:

```bash
uv add google-generativeai
```

7. Finally, execute the project using below command:

```bash
uv run memory # where memory is custom built command
```

## User memory

You can store the users conversation on the third party server called - Mem0 and its process is mentioned below:

- Go to the Mem0 website - [Mem0 Login](https://app.mem0.ai/login).
- Secondly, Go to the `API Keys` section and create API key.
- Copy the API and paste that key into your project's `.env` file.
- Import the `MemoryClient` & `dotenv` as follows:

  ```python
  import os
  from mem0 import MemoryClient
  from dotenv import load_dotenv
  ```

- Get Gemini & Mem0 API keys

  ```python
  load_dotenv()
  GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
  MEM0_API_KEY = os.getenv("MEM0_API_KEY")
  ```

- Create User's client object

  ```python
  client=MemoryClient(api_key=MEM0_API_KEY)
  ```

- Create a list of prompts or messages that need to save in user's client object

  ```python
  prompts=[
    {"role":"user", "content":"Hi there! I am planning a vacation and could use some advice."}
    ,{"role":"assistant", "content":"Hello! I'd be happy to help with your vacation planning. What kind of destination do you prefer?"}
    ,{"role":"user", "content":"I am more of the beach person then a mountain person."}
    ,{"role":"assistant", "content":" That's interesting. DO you like Hotels or Airbnb?"}
    ,{"role":"user", "content":"I like Airbnb more."}
    ]
  ```

- Add above prompts into the `MemoryClient`.
  ```python
  client.add(prompts,user_id="Naveed")
  ```

**Note: Here `Prompts` and `user_id` is used as static for understanding purposes but you can try dynamic `user_id` by linking it the profile id of login person with their prompts.**

- Finally inside the `crew()` add following to configure the User's memory.

```python
crew = Crew(
    agents=[agent],  # will be same code as we studied in pevious section
    tasks=[task],   # will be same code as we studied in pevious section
    memory=True, # Now your crew is enabled to save all the things in its default folder storage.
    memory_config={
    "provider":"mem0",
    "config":{"user_id":"Naveed",}
    },
```

**Note: With above changes in your code you can enable the user's memory in your poroject and all the memory will be saved in the Memory section of your Mem0 account.**
