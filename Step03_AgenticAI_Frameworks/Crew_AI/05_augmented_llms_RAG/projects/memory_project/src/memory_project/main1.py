from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
# from crewai.memory.storage import LTMSQLiteStorage, RAG Storage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage
from crewai.memory.storage.rag_storage import RAGStorage
from typing import List, Optional
import os
from mem0 import MemoryClient  # import it only if you want to save the user's memory
from dotenv import load_dotenv


# Get the GEMINI API key & mem0 API key if you wanted to save the user's memory
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MEM0_API_KEY = os.getenv("MEM0_API_KEY")
# if you want to create a user's memory below two steps are essential otherwise these two steps.

# Step# 1 - Create a user's client object
MEM0_API_KEY = MEM0_API_KEY.strip()
client=MemoryClient(api_key=MEM0_API_KEY)  # imported from above mentioned command


prompts=[
    {"role":"user", "content":"Hi there! I am planning a vacation and could use some advice."}
    ,{"role":"assistant", "content":"Hello! I'd be happy to help with your vacation planning. What kind of destination do you prefer?"}
    ,{"role":"user", "content":"I am more of the beach person then a mountain person."}
    ,{"role":"assistant", "content":" That's interesting. DO you like Hotels or Airbnb?"}
    ,{"role":"user", "content":"I like Airbnb more."}
    ]

client.add(prompts,user_id="Naveed") # You can make the user_id as dynamic and can link with user's login profile. 

# Step # 2 - Only change in crew agent and add `memory_config`. memory _config is defined in the crew().


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
    memory_config={
        "provider": "mem0",
        "config": {
            "user_id": "Naveed",
            "client": client 
        }
    },
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
    ),  # Step # 2 of user memory
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


