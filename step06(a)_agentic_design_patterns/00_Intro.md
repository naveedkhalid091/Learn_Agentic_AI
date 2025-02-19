## Anthropic's Design Patterns for AI Agents:

Anthropic, a company specializing in AI research, has **outlined methodologies for constructing AI Agents**, emphasizing a progression from foundational components to more complex systems. Their approach can be categorized into two primary types:

### 1. **Workflow Based Agents:**

These agents operate based on predefined sequences of steps to accomplish specific tasks. Developers design structured workflows that the agent follows methodically. For instance, in generating a blog post or thesis, the agent might:

- **Step 1:** Gather relevant information from various sources.
- **Step 2:** Verify the accuracy and credibility of the collected content.
- **Step 3:** Compose the draft of the thesis or blog post.
- **Step 4:** Check for plagiarism and ensure originality.
- **Step 5:** Present the final output to the user, including a plagiarism report.

This structured approach ensures consistency and reliability in task execution.

### 2. **Autonomous Agents:**

Autonomous agents possess the capability to operate independently, making decisions and adapting to new information without explicit step-by-step instructions. They are designed to handle complex, dynamic tasks by setting goals and determining the best actions to achieve them. For example, an autonomous agent tasked with market analysis might:

- Identify emerging trends by analyzing real-time data.
- Adjust its analytical models based on the latest information.
- Provide insights and recommendations without human intervention.

These agents are particularly useful in environments where flexibility and real-time decision-making are crucial.

#### **The sub parts of workflows:**

i) **Building block: The augmented LLM:**

- An augmented large language model (LLM) is the core component that gets extra abilities. Besides generating text, it can:

  - Look up information (retrieval).
  - Use external tools (like calculators or web search).
  - Remember previous conversations or data (memory)

    - Enhancing LLMs with RAG, external tools and memory is a robust approach to addressing the limitations of a standalone model. Tailoring these augmentations to the specific use case—and keeping their interfaces simple and well-documented—is critical for reliability and ease of debugging.

  **Note: We have learnt to built above augmented LLM in RAG Section.**

ii) **Workflow: Prompt chaining:**

- A method where a complex task is broken down into a series of smaller, linked steps. Each step builds on the previous one.

**Example:**
Think of writing a research paper:

- Step 1: Gather background information.
- Step 2: Create an outline.
- Step 3: Write a draft based on the outline.
- Step 4: Revise and refine the draft.

Each step helps ensure that the final product is detailed and accurate.

iii) **Workflow: Routing:**

Routing classifies an input and directs it to a specialized followup task. Without this workflow, optimizing for one kind of input can hurt performance on other inputs.

**Example of understanding a routing system:**

- Imagine a busy mailroom where every letter is checked and then sent to the right department based on its content. That's what routing does for LLMs. Instead of one model handling every request, a routing system examines each input and decides which specialized model or processing pathway is best suited to handle it. Similarly, the router looks at your prompt and sends it to the model that excels in that area.

- **Sorting by Expertise:** If a letter is about creative ideas, it goes to the creative team; if it's a technical question, it goes to the technical experts.

- **Optimizing Results:** This targeted approach means every task is handled by the most capable “expert,” improving the overall quality and efficiency of the response.

  - **Examples where routing is useful:**

    - Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools.

iv) **Workflow: Parallelization**

- LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically.

- Imagine you have a big job to do. Instead of doing it step by step, you can split the work so multiple people or processes work on it at the same time. In LLM workflows, parallelization works in two ways:

  - **Sectioning:** You break the big job into smaller, independent pieces that can be done at the same time. Once all the pieces are completed, you put them back together for the final result. Sectioning can drastically reduce processing time for large tasks.

  - **Voting**: You run the same task several times (or use several models) to get different answers. Then you compare these answers and choose the best one. Voting helps balance the risk of errors by considering multiple outputs.

v) **Workflow: Orchestrator-workers:**

- In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.

  - **For Example:**

    - Orchestrator-workers workflow is basically the combination of **Routing workflow** & **Parallelization Workflow**.

  - Consider **Orchestrator-workers workflow** as a head chef whcih first sort the food order **(Routing part)** the chef then splits the order into separate dishes and assigns each dish to a different cook so they can prepare everything at the same time—**that’s the parallelization part** Finally, once all the dishes are ready, the head chef brings all the dishes together and presents a complete meal to the customer (synthesizing of order).

vi) **Workflow: Evaluator-Optimizer**

- In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop and finall response is sent to the users if the evaluation and feedbackback are good.

  - **For Exmaple:**

    - Imagine you're writing an essay. You write a first draft, then hand it to an editor who reviews it, points out mistakes, and suggests improvements. You then revise the draft based on that feedback, and the cycle repeats until the essay meets your standards.
    - In the evaluator-optimizer workflow, one LLM acts as the "writer" that generates a draft response, while a second LLM plays the role of the "editor" that reviews the draft, evaluates its quality, and provides feedback. The writer then uses this feedback to improve its answer. This loop continues until the response is good enough according to the defined criteria.
