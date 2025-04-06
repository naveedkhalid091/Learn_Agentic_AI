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

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
SERPER_API_KEY=os.getenv("SERPER_API_KEY")
MODEL=os.getenv("MODEL")

# llm 

llm1=LLM(model="gemini/gemini-2.0-flash")

# embedder_config

embedder_config ={
    "provider":"google",
    "config":{
        "model":"models/text-embedding-004",
        "api-key":os.getenv("GEMINI_API_KEY")
        }
 }

# Instantiate Tools

docs_tool=DirectoryReadTool(
    directory='./blog-posts',
    embedder=embedder_config)

file_tool=FileReadTool(embedder=embedder_config)
search_tool=SerperDevTool(embedder=embedder_config)
web_rag_tool=WebsiteSearchTool(embedder=embedder_config)


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
    # planning=True, # Enable Planning feature - for this crewai decide on its own what to search and when to search, is the seached content is enough or not? Shall I need to search again? 
    # planning_llm=llm1, # This is an another planning agent
    # embedder=embedder_config
)

def my_writter():
    result=crew.kickoff()
    print(result)

