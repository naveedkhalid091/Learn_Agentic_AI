## Memory:

CrewAI’s memory system is designed to help AI agents "remember" important information during their tasks.It uses different types of memory whichare covered below:

### Introduction to Memory Systems in CrewAI

The crewAI framework introduces a sophisticated memory system designed to significantly enhance the capabilities of AI agents. This system comprises **short-term memory**, **long-term memory**, **entity memory**, **contextual memory**, and **user memory** each serving a unique purpose in aiding agents to remember, reason, and learn from past interactions.

### 1. Memory types:

- **Short-Term Memory (STM):**
  - **What it does:** Temporarily holds recent interactions or outcomes. It keeps track of recent interactions but doesn’t last forever.
  - **Simple Analogy:** Think of it like a sticky note that keeps track of what just happened so the agent can refer to it during the current conversation or task.
  - **Key Point:** It uses a technique called **RAG** (Retrieval-Augmented Generation) to fetch relevant data quickly.
- **Long-Term Memory (LTM):**

  - **What it does:** Stores important learnings and insights from past tasks over a longer period.

  - **Simple Analogy:** Imagine a diary where the agent writes down useful information from past experiences to improve future decision-making.

- **Entity Memory:**
  - **What it does:** Organizes and keeps track of specific entities (like people, places, or concepts) encountered during interactions.
  - **Simple Analogy:** It’s like having a detailed contact list that helps the agent remember important details about key items or individuals.
- **Contextual Memory:**
  - **What it does:** Combines information from short-term, long-term, and entity memory to provide a complete picture of the conversation or task. It helps AI understand the current conversation or task by recalling relevant details.
  - **Simple Analogy:** Think of it as the storyline in a book that ties all individual notes (memories) together, ensuring responses are coherent and relevant over time.
- **User Memory:**
  - **What it does:** Stores user-specific information and preferences to offer a more personalized interaction.
  - **Simple Analogy:** Like a personal assistant who remembers your likes, dislikes, and past requests to better serve you in the future.
  - For this you have to use the additional package called **`mem0`**. With this package users prompt memory can be saved and managed.\*\*

### 2. How Memory Systems Empower Agents:

- **Contextual Awareness:** With short-term and contextual memory, agents gain the ability to maintain context over a conversation or task sequence, leading to more coherent and relevant responses.
- **Experience Accumulation:** Long-term memory allows agents to accumulate experiences, learning from past actions to improve future decision-making and problem-solving.
- **Entity Understanding:** By maintaining entity memory, agents can recognize and remember key entities, enhancing their ability to process and interact with complex information.

### 3. Implementing Memory in Your Crew:

- **Enabling Memory system:** When configuring a crew, you can enable and customize each memory component to suit the crew’s objectives and the nature of tasks it will perform. By default, the memory system is disabled, and you can ensure it is active by setting **`memory=True`** in the crew configuration.
- **Embeddings:** The memory will use OpenAI embeddings by default, but you can change it by setting **embedder** to a different model.
- The ‘embedder’ only applies to **Short-Term Memory** which uses **Chroma** for RAG. The **Long-Term Memory uses SQLite3** to store task results. Currently, there is no way to override these storage implementations.
- In the code you will just write the path of long_term, short_term and entity memory, crewAi will automatically creat folders against your path and will automatically manage where the content will go, either in long term or short term memory etc. The data storage files are saved into a platform-specific (either in your project or on the Cloud storage) location.
- The name of the project can be overridden using the **CREWAI_STORAGE_DIR** environment variable.

For further explanation please read the `01(b)memory_codding.md` section.

**Note: You can save these memories in specific locations either in database or in drive etc and use the required memory when needed.**
