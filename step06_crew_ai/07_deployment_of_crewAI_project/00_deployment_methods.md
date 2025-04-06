## Deployment Methods:

There are three methods to deploy your CrewAI project.

CrewAI deployment is only available for Enterprises, means that the **deployment services are paid** however your can deploy your one project for free in the crewAI but you can **process only first 50 requests** from the deployed project, after that you have to buy the crewAI services.

When your crew project is running perfectly fine then you can decide to pay CrewAI.

However, lets discuss the three deployment methods:

1. **Deploy through Github:** - Create your project, Push on Github and finally connect using `cicd`. Whenever you will push new things or updates then CrewAI will encorporate those updates automatically. (We will use this method many times)

2. **Deploy using CrewAI's Chatbot:** - Talk you the CrewAI chatbot, based on your requirments, it will ask your project keys from you and will perform the required coding and finally show you a graphical project/crew with agents detail. After that you can deploy your proejct after visualization. (This method is well suited related to the non-technical background, means if you don't know coding and still want to create your agent then this Chatbot will help you to create an agent for you)

3. **Delpoy through CrewAI pre-defined given patterns:**

Now lets discuss the steps involved from creating your project till the end of deployment.

**Step-1** : Create your flow project

```bash
crewai create flow ProjectName
```

**Step-2**: Navigate to your project director:

```bash
cd ProjectName
```

**Step-3** : Open your project in cursor or VScode:

```bash
code . # or write `cursor .` command if you have installed and configured cursor in your laptop
```

**Step-4** : Go to the `.env` file and set the API keys and Model name:

```bash
GEMINI_API_KEY= WRITE_KEY_HERE
MODEL=WRITE_YOUR_MODEL_PATH_HERE   # e.g MODEL=gemini/gemini-2.0-flash
```

**Step-5** : You will now write your code and create your project, but here we are only learning to deploy the project that's why we will not write code and simply deploy the readymade project called `poem flow` that was created through above command:

**Step-6:** Before Deployment, and after writing code, we will first `sync` the project as follows:

```bash
uv sync
```

**Note:**
Running the uv sync command is essential because it synchronizes your project’s virtual environment with the exact dependencies and versions defined in your lockfile (uv.lock). CrewAI uses uv for managing dependencies, so before deploying, you need to make sure that:

• **Environment Consistency:** The environment reflects all the changes made in your pyproject.toml and lockfile, ensuring that every dependency is installed at the correct version.

• **Reproducibility:** By syncing, you guarantee that the project behaves the same way across different setups, reducing the risk of missing or incompatible packages.

• **Clean State:** It removes any extraneous packages that aren’t part of your defined
dependencies, keeping the environment lean and predictable.

Without this step, your deployment might run with outdated or incomplete dependencies, potentially causing runtime errors.

**Step-7** : Write below command to activate your virtual environment using cmd.

```bash
.venv\Scripts\activate.bat  # for Powershell write .\.venv\Scripts\Activate.ps1
```

If due to any reason, you wanted to **deactivate** your virtual environment then simply write `deactivate` in your terminal.

**Note: Activation of your Virtual environment is necesary because it is important to keep your project’s dependencies separate from other projects and the global Python installation. This isolation prevents conflicts between different versions of packages and ensures that your project runs with exactly the libraries and versions it requires.**

**Step-8** : Run your project on cli or locally to check whether it is running or not?, in our example of project1 available inside the `Deplyed_project>project1`, this is the ready made peom-flow project so simply write below command to check the project is runnig? However you can define other custom commands of your project as we discussed in previous sections.

```bash
uv run kickoff
```

**Note:** The `poem-flow` project will not be returning anything as this was a ready made project, only a **print** function will be available, as the print function only used to print the results in the CLI, that's why we will add the return statement into code so that cloud deployment may return data from `return` key word.

Add following into `save_poem` function

```py
return {"poem":self.state.poem, "sentence_count":self.state.sentence_count , "author":"Naveed Khalid"}
```

**Step - 9:** Write below command in the terminal

```bash
crewai run
```

The above command will through error **Failed to spawn: `run_crew`**, **Caused by: `program not found`**.

You need to configure `run_crew` command in `.toml` file as follows:

```bash
run_crew= "project1.main:kickoff"  # where project1=projectName
```

As per the standards, now our project is ready for deployment.
