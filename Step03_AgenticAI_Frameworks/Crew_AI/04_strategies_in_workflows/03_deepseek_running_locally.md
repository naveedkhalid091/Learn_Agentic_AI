## How to Install DeepSeek (Chinese LLM) locally and Integrate Deepseek into Your Project Using Ollama with Flow and LiteLLM:

### What is Ollama?

Ollama is a **platform** that focuses on **running open source** language models—often locally.

## 1. Installation of ollama and Deepseek into your local Machine:

1. Go to Google and Search **ollama**.
2. Download ollama into your local machine.

   **Note: You can read the ollama documentation from the link mentioned at the bottom of the page. or you can also read it from - [ollama Docs](https://github.com/ollama/ollama/tree/main/docs)**

3. Install the ollama after downlaoding it.
4. Check the version of ollama in your terminal after sucessfull installation:

   ```bash
   ollama --version
   ```

5. To check the list of supported models in ollama, you can click the link - [ollama Models](https://ollama.com/search) & you can click on the desired model you want to download e.g. click on the `deepseek-r1`, you will see the list of its available versions i.e. 1.5b,7b,8b, 70b, 671b etc.

   **_Very Important Note: We will run the most lightweight llm in our example becasue to run the llm locally we need a `V-RAM` in our machine (V-RAM is a virtual RAM of GPU) So, ultimately you need a GPU i you need `V-RAM`. However some lightweight llms can also be run on the CPUs but when you will process havy tasks from that llms then your laptop can be heat-up. So you need extra care in running your llm in your local machine._**

6. The most lightweight llm of deepseek-r1 is `1.5b version`.
7. Write below command in terminal after above steps to use the `1.5b` version of deepseek-r1 into your loal machine.

```bash
ollama run deepseek-r1:1.5b
```

8. After sucessfull installation, deepseek will automatically run in the terminal, quit deepseek from the terminal by pressing `ctrl+d`.

9. To check how many `llms` you currently have in your system you can write below command in the terminal

```bash
ollama list
```

## 2. Integration of Deepseek with your project:

1. Create a project using flow:

```bash
crewai create flow ProjectName
```

Suppose your project name is `deepseek_project`

2. Navigate to the project directory

```bash
cd deepseek_project
```

3. Go to the `.env` file and write model name & Base URL.
   **_(You will not be required an API key because the model in now locally installed in your machine)_**

```.env
MODEL=ollama/deepseek-r1:1.5b
BASE_URL=http://127.0.0.1:11434
```

**NOTE: Your base URL is the localhost address where ollama is running & if you have not changed the settings then the default address of ollama is `http://127.0.0.1:11434`, Secondly, you don't need to start the localhost, ollama localhost automatically start at its default location.**

4. With above mimimum changes or configurations your crew project will converts into ollama's specified model.

5. Finally run the below built-in command to check if the peomflow (built-in) run on your computer or not?

```bash
uv run kickoff
```

#### I have varified that the built-in peomflow is running on my local machine (terminal) & saved a file `poem.txt` and written content inside the txt file. now its your turn to check.

Note: As you hav selected the lightllm model, so note it down that its reasoning capability is not so good.
