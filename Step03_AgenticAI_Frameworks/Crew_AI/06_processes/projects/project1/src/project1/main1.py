from crewai import Crew, Agent, Task, Process, LLM
import os
from crewai_tools import DirectoryReadTool, FileReadTool, SerperDevTool, WebsiteSearchTool
# from dotenv import load_dotenv
# load_dotenv()

# Setup API Keys & MODEL

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
SERPER_API_KEY=os.getenv("SERPER_API_KEY")
MODEL=os.getenv("MODEL")

## llm 
llm1=LLM(model="gemini/gemini-2.0-flash")

# Instantiate tools

docs_tool=DirectoryReadTool(directory='./blog-posts')
file_tool=FileReadTool()
search_tool=SerperDevTool()
web_rag_tool=WebsiteSearchTool()


# embedder_config

embedder_config ={
    "provider":"google",
    "config":{
        "model":"models/text-embedding-004",
        "api-key":os.getenv("GEMINI_API_KEY")
        }
 }


# Define your agents

researcher=Agent(
    role="Researcher",
    goal="conduct through research and analysis on AI and AI Agents", 
    backstory="You are an expert researcher, specialized in technology, softwere Engineering, AI and startups.",
    llm=llm1,
    tools=[search_tool, web_rag_tool],
    allow_delegation=False
)

writter=Agent(
    role="Senior Writer",
    goal="Create Compelling content about AI and AI Agents", 
    backstory="You are a senior writter, speciallized in technology, softwere engineering, AI and startups",
    llm=llm1,
    tools=[docs_tool,file_tool],
    allow_delegation=False
)

# Define your Task - task is assigned to crew. 

task=Task(
    description="Generate a list of five interesting ideas for an articles, then write one captivating paragraph for each idea that showcases the potential of a full article on this topic. Return the list of ideas with their paragraphs and your notes",
    expected_output="Five bullet points, each with a paragraph and accompanying notes.",
    # we will not assign agents here because manager_agent will decide to whome the task is assigned. 
)

# Define the Manager Agent, this agent manages the other agents defined in the project
manager=Agent(
    role="Project Manager",
    goal="Efficiently manage the crew and ensure high-quality task completion.",
    backstory="You are an experienced project manager, skilled in overseeing complex projects and guiding teams to sucess. Your role is to coordinate the efforts of crew members, ensuring that each task is completed on time and to the highest standard.",
    allow_delegation=True, # `True` is compulsory in manager agents, this enables this agent to delegate tasks.  
    llm=llm1
)

# Instantiate your crew with a custom manager

crew=Crew(
    agents=[researcher, writter],
    tasks=[task],
    manager_agent=manager,
    function_calling_llm=llm1, 
    process=Process.hierarchical,   # 
    verbose=True,
    embedder=embedder_config
)

def my_process():
    result=crew.kickoff()
    from IPython.display import Markdown
    Markdown(result.raw)


