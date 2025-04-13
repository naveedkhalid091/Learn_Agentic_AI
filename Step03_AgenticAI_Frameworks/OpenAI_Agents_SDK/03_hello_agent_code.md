## First Agent using UV:

1. Write below command to initialize your first project using UV.

   ```bash
       uv init --package ProjectName
   ```

   Note-1: The command `uv init ProjectName` (This is for stand alone app) can also be use but it is used when you’re building any standalone application that you don’t necessarily plan to publish as a reusable library but use the `--package` (This is for full-fledged Python package) flag if you intend to publish your code to PyPI (or another index), or when you want a clean library structure for reuse across multiple projects.

   Note-2: The **init**.py file inside src/project_name/ has two main roles:

   - **Marks the folder as a Python package**.
   - **Runs initialization** code when the package is imported.
     For example, in the hello_agent project’s `pyproject.toml` file, you'll see `hello-agent = "hello_agent:main"` under [project.scripts]. When you `run uv run hello-agent`, it will execute the code in **init.py** — even though the file isn't mentioned explicitly.

2. Navigate to the projec's directory.

```bash
cd ProjectName
```

3. Open your prjoct in IDE, i.e VS-code or Cursor.

```bash
code . # cursor .
```

4. Run the created project to test whether it is correclty built? using the below command:

Note: This command will also create the virtual environment of your project.

```bash
uv run hello-agent

# where hello-agent is project name, this variable is mentioned in [project.scripts] inside the .toml file.
```

**_Note: The command to run the project is assigned under the [project.script] section. The syntax for defining a command in the `.toml` file is: `variableName = ProjectFolderPath:functionName`. The detail is mentioned inside the crewai framework learning, as we had studied that framework first._**

5. Add OpenAi agents package into your project as

```bash
uv add openai-agents
```

Note: If you wanted to run the file instead of packages, then the method is same as running the packages as follows:

For Example: you wanted to run a file name called main.py then you will use following command:

```bash
uv run main.py
```

Untill Now we have learnt to add the agents in our project moving forward we will be using & creating the agent.
