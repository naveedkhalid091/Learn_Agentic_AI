## Testing:

This part explains how to test your CrewAI's crew and evaluate the performance of your crew.

### Introduction:

Testing is a crucial part of the development process, and it is essential to ensure that your crew is performing as expected. With crewAI, you can easily test your crew and evaluate its performance using the built-in testing capabilities.

### Using the Testing Feature:

You just have to give the following CLI command to test your crew:

```bash
crewai test
```

This command will run your crew for a specified number of iterations and provide detailed performance metrics.

The parameters are **n_iterations** and **model**, which are optional and default to **2 iterations** and **gpt-4o-mini** respectively. For now, the only provider available is OpenAI,

**Important Note: `gpt-4o-mini` is paid and if you wanted to test your crew then you will have to buy subscription.**

If you want to run more iterations or use a different model, you can specify the parameters like this:

```bash
crewai test --n_iterations 5 --model gpt-4o
```

or using the short forms:

```bash
crewai test -n 5 -m gpt-4o
```

When you run the crewai test command, the crew will be executed for the specified number of iterations, and the performance metrics will be displayed at the end of the run.

A table of scores at the end will show the performance of the crew in terms of the following metrics:

| Task / Crew / Agents   | Run 1 | Run 2 | Avg. Total | Agents                           | Additional Info                |
| ---------------------- | ----- | ----- | ---------- | -------------------------------- | ------------------------------ |
| **Task 1**             | 9.0   | 9.5   | 9.2        | Professional Insights Researcher |                                |
| **Task 2**             | 9.0   | 10.0  | 9.5        | Company Profile Investigator     |                                |
| **Task 3**             | 9.0   | 9.0   | 9.0        | Automation Insights Specialist   |                                |
| **Task 4**             | 9.0   | 9.0   | 9.0        | Final Report Compiler            | Automation Insights Specialist |
| **Crew Average**       | 9.00  | 9.38  | 9.2        |                                  |                                |
| **Execution Time (s)** | 126   | 145   | 135        |                                  |                                |

The example above shows the test results for two runs of the crew with two tasks, with the average total score for each task and the crew as a whole.
