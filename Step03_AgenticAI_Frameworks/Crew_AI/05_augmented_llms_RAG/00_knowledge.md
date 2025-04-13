## Knowledge

What is knowledge in CrewAI and how to use it.

## What is Knowledge?

Knowledge in CrewAI is a powerful system that allows AI agents to access and utilize external information sources during their tasks. This concept is similar to the RAG system which we have studied earlier, but CrewAI has made the RAG process very simple and easy to code.

### Supported Knowledge Sources

CrewAI supports various types of knowledge sources out of the box:

- Text Sources:
  - Raw strings
  - Text files (.txt)
  - PDF documents
- Structured Data :
  - CSV files
  - Excel spreadsheets
  - JSON documents

### Key benefits of using Knowledge (RAG):

- Enhance agents with domain-specific information: If you are an accountant and working in the chartered accountant's firm then you can enhance the knwoldege of agent with your firm related information.
- Support decisions with real-world data: With your existing embedded data, you can help in your decisions.
- Ground responses in factual information: You can get response from the LLM based on the factual or real time data.

You only have to call the relevent `knowledge-source` function and place the path into that function. means if you have data in PDF file then you first have to define the pdf path and then assgin that PDF knowledge source into the knowledge source function to access the information. - For Example: IF you have pdf documents of PDF Knowledge source then you have to import `PDFKnowledgeSource` and for web content you have to import `CrewDoclingSource` etc. - You must read the documentation for which function to call and which one to import for related files.

The link of Knowledge/RAG in CREWAI is here: [knowledge/RAG DOCS](https://docs.crewai.com/concepts/knowledge).

However, I have just mentioned only one example of `stringknowledgesource`. You can try other methods of using PDF,Excel etc by reading the official documentation link above.

The `stringknowledgesource` project coding example is given below:

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
import os

# Get the GEMINI API key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Create a knowledge source
content = "Users name is Naveed. He is 30 years old and lives in Islamabad,Pakistan. Working as a sub-contractor at Johal & Co"
string_source = StringKnowledgeSource(
    content=content
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
    embedder={
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": GEMINI_API_KEY,
        }
    }
)

task = Task(
    description="Answer the following questions about the user: {question}",
    expected_output="An answer to the question.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
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

def my_knowledge():
    result = crew.kickoff(inputs={"question": "What city does Naveed live in and how old is he?"})
    print(result)
```

5. Create a variable in toml file under the [project.script] to run the above project.

```toml
kn="01_knowledge.main1:my_knowledge"
```

6. Install google generative AI as follows:

```bash
uv add google-generativeai
```

7. Finally, execute the project using below command:

```bash
uv run kn # where kn is custom built command
```
