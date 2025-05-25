## **Agents Architecture:**

Before learning about any sepcific **Agentic framework**, lets discuss what is the current architecture of AI Agents. (it will change over the time).

Previosuly when Chatbots were introduced, the chatbots were only integrated with the LLMs only now AI Agents have been introduced with following features/layers available in it.

1. **LLM (Stateless):** Takes an input and generates outputs such as text, audio, it acts like a brain of machine.
2. **RestAPIs:** connecting with RestAPIs, LLM can connect with the external inforamtion including real time information, this feature acts like a hand and eyes of machine which enables it to reach and view th external internet world.
3. **Chat Completion/Response APIs.** connectings with the Response APIs, it enables how to process and manage actions (tool calling) based on the external information gethered from RestAPIs.
4. **Agent Loops (Agentic Frameworks):** Agent Loops are basically agentic frameworks, which enables the features of customization, consistent behaviour and complex decision making in an agent.
5. **Memory:** Stores data from past interactions, giving the agent a memory to recall previous inputs, actions, and decisions.

### **Lets discuss above in Detail:**

- LLM alone can't act like an agent, all above intergrations makes the chatbot to act like an agent.

1. **LLM [stateless]:**

   - **What It Is:** The base layer, a Large Language Model (LLM) like GPT, described as "stateless."
   - **What It Does:**

     - Takes an input and generates outputs such as text, audio.
     - Processes each request independently, without retaining any information from prior interactions.

   - **Drawbacks:**
     - **No Memory:** Being stateless means it forgets everything after each interaction, like a person with no short-term memory. This makes it unsuitable for tasks requiring continuity, such as ongoing conversations or multi-step processes. This drawback will achieved by **integrating memory** into LLM
     - **No external Interactions:** The LLM alone can't access real-time data or interact with external systems. LLM right now is like having a brilliant thinker with no hands or eyes to engage with the world. this will be achived from **RestAPIs**.
     - **No intelligent responses and tool management**: It means if LLM is enabled to get external or real time information through the RestAPIs, LLM is still not capable how to use and response on that external information, This drwaback will be removed by integrating **Chat completion/Response APIs.**
     - **No customization or consistant behaviour**: even integrating all the features above still we can't create industry specific or consistent agents. This is made possible thourgh **Agentic Frameworks**:

2. **RestAPIs:**

   1. **What It Is:** A communication layer that uses HTTP requests to connect the system to external services.
   2. **What It Does:** 1. Allows the agent to retrieve data (e.g., current weather). 2. Serves as a bridge between the LLM and the external world.

3. **Chat Completions/Response API:**

   1. **What It Is:** A layer leveraging OpenAI’s Chat Completions API to produce responses and handle tool interactions.
   2. **What It Does:**
      1. Generates the agent’s outputs, such as text replies or decisions to invoke tools.
      2. Works with the Rest API to execute actions based on the generated responses.

4. **Agent Loop (Agentic Framework)**:

   1. **What is this:** The operational core of the agent, implemented using the OpenAI Agents SDK.
   2. **What It Does:**

      1. Manages the agent’s workflow, including:

         1. System Prompt: Sets the agent’s goals and personality (customization defined here).
         2. Tool Calling: Determines when and how to use external tools.
         3. HandOff: Potentially delegates tasks to other systems or agents.

      2. Incorporates Guardrails to ensure safe and appropriate inputs and outputs.

