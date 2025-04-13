## Strategies to Follow in the CrewAI flows:

There are commonly two types of flow strategies you can follow, both approaches ultimately use the same underlying language model (often via LiteLLM under the hood), but they offer very different levels of abstraction and control.

Your choice depends on the complexity of your task and the level of orchestration you require.

### 1. Use a **LiteLLM strategy** for simple flows:

### 2. Use a combination of **crews/agents/tasks strategy** for more complex flows:

When to Use Which Strategy:

**Use LiteLLM When:**

- You have a single step, self-contained query or task.
- You’re in the early prototyping phase and want minimal overhead.
- The task does not require delegation or multi-step reasoning.

**Use Crews/Agents/Tasks (CAT) When:**

- You need to solve a problem that requires multiple steps, coordination, or decision-making.
- Different agents or tasks are best suited for different aspects of the problem.
- You’re building production-grade applications that require clear workflow control, error handling, and state management.

In practice, many applications blend the two: you might build a crew of agents where each agent makes its LLM calls via LiteLLM. This way, you get both the simplicity of a unified LLM interface and the power of structured collaboration.

**Note:** Navigate to the **crews_agents_task > project1** folder to see examples of each of the strategies and you can also navigate to the next section `01_strategies_implement_in_code.md` where step wise explanation is written.

Read documentation of the Crews from here: [Crews](https://docs.crewai.com/concepts/crews)
