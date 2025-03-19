## Tools:

A tool in CrewAI is a skill or function that agents can utilize to perform various actions. This includes pre-defined tools from the [CrewAI ToolKit](https://github.com/crewAIInc/crewAI-tools) and [Lanchain Tools](https://python.langchain.com/docs/integrations/tools/), enabling everything from simple searches to complex interactions and effective teamwork among agents.

### Key Characteristics of Tools:

- **Utility:** Tools crafted for tasks such as web searching, data analysis, content generation, and agent collaboration.
- **Integration:** Tools boost agent capabilities by integrating into the agents' workflow.
- **Customizability/flexibility:** Tools provide the flexibility to develop custom tools or utilize existing ones, depending on the needs of agents.
- **Error Handling:** Tools incorporates robust error handling mechanisms to ensure smooth operation.
- **Caching Mechanism:** Tools have the intelligent caching mechanism to optimize performance and reduce redundant operations.

### Using CrewAI Tools

To enhance your agents’ capabilities with crewAI tools, begin by installing into your project that you have created using `crewai create flow ProjectName`:

```bash
pip install crewai[tools]
```

and then write following code in main1.py file.

```python
from crewai_tools import (
  DirectoryReadTool, # Facilitates reading and processing of directory structures and their contents.
  FileReadTool,       # Enables reading and extracting data from files, supporting various file formats.
  SerperDevTool,       # Connected to serper.dev website that's why we need API keys to use this
  WebsiteSearchTool  # A RAG tool for searching website content, optimized for web data extraction.
)
from crewai import Crew, Agent, Task, LLM
from langchain_google_genai import ChatGoogleGenerativeAI # install it first if not already installed

import os
# from dotenv import load_dotenv
# load_dotenv()

# Setup API Keys & MODEL

GEMINI_API_KEY=os.environ.get("GEMINI_API_KEY")
SERPER_API_KEY=os.environ.get("SERPER_API_KEY")
MODEL=os.environ.get("MODEL")

# llm

llm1=LLM(model="gemini/gemini-2.0-flash")

# Instantiate Tools

docs_tool=DirectoryReadTool(directory='./blog-posts')
file_tool=FileReadTool()
search_tool=SerperDevTool()
web_rag_tool=WebsiteSearchTool()


# embedder_config

embedder_config ={
    "provider":"gemini",
    "config":{
        "model":"models/text-embedding-004",
        "api-key":os.getenv.get("GEMINI_API_KEY")
        }
 }

# Create multi-agents

# 1. Market researcher agent

researcher=Agent(
    role="Market Research Analyst",
    goal="Provide up-to-date market analysis of the AI industry",
    backstory="An expert analyst with keen eye for market trends",
    tools=[search_tool, web_rag_tool],
    verbose=True
),

writter=Agent(
    role="Content Writter",
    goal="Craft engagging blog posts about the AI industry",
    backstory="A skilled writter with a passion for technology.",
    tools=[docs_tool, file_tool],
    verbose=True
)

# define tasks

research=Task(
    description=" Research the latest trends in the AI industry and provide a summary",
    expected_output="A summary of top 3 trending developments in the AI industry with a unique perspective on thier significance",
    agent= researcher,
)

write=Task(
    description="Write an engaging blog post about AI industry, based on the research analyst's summary  ",
    expected_output="A 4 paragraph blog post formatted in markdown with engagging, informative content",
    agent=writter,
    output_file= "blog-posts/new-post.md"
)

crew=Crew(
    agents=[researcher,writter],
    tasks=[research,write],
    verbose=True,
    planning=True, # Enable Planning feature - for this crewai decide on its own what to search and when to search, is the seached content is enough or not? Shall I need to search again?
    planning_llm=llm1, # This is an another planning agent
    embedder=embedder_config
)

def my_writter():
    result=crew.kickoff()
    print(result)
```

**Note: Above is generating an OpenAI key error, I will fix it later on.**

Lets discuss the ways for creating custom tools, there are two methods of creating tools in crewAI.

1. import the tools class and create your own new class and make a function called `_run` inside your class and finally process your business logic or parameters.
2. import a decorator and place that before the start of any other functions, such functions will be considered as your tool.

You basically call a tool/function, that function could wrap any of the below:

- A function to search anything from the web.
- A function to search anything from your defined folders.
- A function might be connected to your database and work from your database.

You can read about tools from the Official documentation - [CrewAI Tools](https://docs.crewai.com/concepts/tools)
