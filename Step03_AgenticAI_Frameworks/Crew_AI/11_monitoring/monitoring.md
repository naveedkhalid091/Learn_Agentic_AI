## Monitoring of Agents:

## Agents Monitoring Using AgentOps:

**Note: Create your Agent and finalize your code and finally enable monitoring through following plateforms.**

1. Create an API Key from [AgentOps](https://app.agentops.ai).
2. Paste API key into `.env` file.
3. Load API key as follows:

```python
   import os
   from dotenv import load_dotenv, find_dotenv
   load_dotenv(find_dotenv())
```

4. Initalize Agentops as follows in `crew.py`.

   ```python
    agentops.init(api_key=os.getenv("AGENTOPS_API_KEY"))
   ```

5. Install AgentOps thourgh command ` uv add crewai[agentops]`.
6. Initialize AgentOps into your `crew.py` file as:
   ```py
   import agentops
   agentops.init()
   ```

````

6. Finally run the crew through command `crewai run`.

## Monitoring with OpenLIT:

We will learn to monitor our AI Agents in just a single line of code with OpenTelemetry.

### OpenLIT Overview:

**[OpenLIT](https://github.com/openlit/openlit?src=crewai-docs)** is an open-source tool that makes it simple to monitor the performance of AI agents, LLMs, VectorDBs, and GPUs via **its DashBoard** with just one line of code.

It provides OpenTelemetry-native tracing and metrics to track important parameters like cost, latency, interactions and task sequences. This setup enables you to track hyperparameters and monitor for performance issues, helping you find ways to enhance and fine-tune your agents over time.

### Features:

- **Analytics Dashboard:** Monitor your Agents health and performance with detailed dashboards that track metrics, costs, and user interactions.
- **OpenTelemetry-native Observability SDK:** Vendor-neutral SDKs to send traces and metrics to your existing observability tools like Grafana, DataDog and more.
- **Cost Tracking for Custom and Fine-Tuned Models:** Tailor cost estimations for specific models using custom pricing files for precise budgeting.
- **Exceptions Monitoring Dashboard:** Quickly spot and resolve issues by tracking common exceptions and errors with a monitoring dashboard.
- **Prompt Injection Detection:** Identify potential code injection and secret leaks.
- **API Keys and Secrets Management:** Securely handle your LLM API keys and secrets centrally, avoiding insecure practices.
- **Prompt Management:** Manage and version Agent prompts using PromptHub for consistent and easy access across Agents.
- **Model Playground** Test and compare different models for your CrewAI agents before deployment.

### 1. Deploy OpenLIT:

    i) Git Clone OpenLIT Repository

        ```bash
        # use this method is you have valid SSH key registered. otherwise use below method
        git clone git@github.com:openlit/openlit.git
        ```

        OR

        ```bash
        # from your project directory:
        git clone https://github.com/openlit/openlit.git
        ```
    ii) Start Docker Compose:

        - Navigate to the OpenLIT Repo (Created from above step) and Run the below command:

        Note: Before initiating below command you must ensure that you have Docker installed into your machine and the Docker can't be installed without prior installation of WSL2 (Windows Subsystem for Linux 2):
        We will not discuess the installation of Docker and WSL2 here. You can installation of WSL2 and Docker from ChatGPT or from Internet.

        After Installation of Docker Desktop, ensure that Docker Desktop app is also opened and then finally write below command in the terminal:

        ```bash
        docker compose up -d
        ```
        The openlit will be integrated with the docker engine after the above command (you can also view openlit in the Docker UI interface).

### 2. Install OpenLIT SDK:

```bash
uv add openlit  # or pip install openlit
```

### 3. Initialize OpenLIT in your Application:

In your project paste following code into your `crew.py` file:

```py
import openlit

openlit.init(otlp_endpoint="http://127.0.0.1:4318" , disable_metrics=True)
```

Now at this stage your project is connected with the openLIT.

For Safer side run your crew to check if there is any error?

```bash
crewai run
```

Note: You can try other monitoring plateforms as well mentioned in crewAI docs.

After that define your agent, tasks and crew etc.

### Visualize and Analyze:

With the Agent Observability data now being collected and sent to OpenLIT, the next step is to visualize and analyze this data to get insights into your Agent’s performance, behavior, and identify areas of improvement.

Just head over to OpenLIT at 127.0.0.1:3000 on your browser to start exploring. You can login using the default credentials

Email: user@openlit.io
Password: openlituser

Openlit will count and tack the record of total number of requests made to LLMs, cost etc.
````
