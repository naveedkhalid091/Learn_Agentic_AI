## Adding OpenAI Agents SDK into your project:

This envolves to main steps:

1. Create a UV project.
2. Create/add OpenAI Agents SDK into your Project.

### **1. Create a UV project:**

i). Write below command to initialize your first project using UV.

    ```bash
        uv init --package ProjectName
    ```

    Note: You can also write the command `uv init ProjectName` to initialize the project but this is for stand alone `app` means it is used when you’re building any standalone application that you don’t necessarily plan to publish as a reusable library but use the `--package` flag if you intend to publish your code to PyPI (or another index).

    Note-2: The **init.py** file inside src/project_name/ has two main roles:

    - **Marks the folder as a Python package**.

    - **Runs initialization** code when the package is imported.

    - For example, in the hello_agent project’s `pyproject.toml` file, you'll see `hello-agent = "hello_agent:main"` under [project.scripts]. When you `run uv run hello-agent`, it will execute the code in **init.py** — even though the file isn't mentioned explicitly.

ii). Navigate to the project's directory.

    ```bash
    cd ProjectName
    ```

iii). Open your prjoct in IDE, i.e VS-code or Cursor.

    ```bash
    code . # cursor .
    ```

iv). Run the project to test whether it is correclty built? using the below command:

    Note: This command will also create the virtual environment of your project.

    ```bash
    uv run hello-agent
        # where hello-agent is project name, this variable is mentioned in [project.scripts] inside the .toml file.
    ```
    **_Note: The command to run the project is assigned under the [project.script] section. The syntax for defining a command in the `.toml` file is: `variableName = ProjectFolderPath:functionName`. The detail is mentioned inside the crewai framework learning, as we had studied that framework first._**

### **2. Create/add OpenAI Agents SDK into your Project.:**

i) Install OpenAI SDK into your project

    ```bash
      uv add openai-agents # pip install -Uq openai-agents
    ```

    Note: If you wanted to run the file instead of a project, then use below command.

    ```bash
      uv run main.py   # where main.py is file name
    ```
