## Training:

In this Section we will learn to train CrewAI Agents by giving them feedback early on and get consistent results.

### Introduction:

The training feature in CrewAI allows you to train your AI agents using below CLI command.

```bash
crewai train -n <n_iterations>  # you can specify the number of iterations for the training process.
```

During training, CrewAI utilizes techniques to optimize the performance of your agents along with human feedback. This helps the agents improve their understanding, decision-making, and problem-solving abilities.

### Training Your Crew Using the CLI:

To use the training feature, follow these steps:

- Open your terminal or command prompt.
- Navigate to the directory where your CrewAI project is located.
- Run the following command:

```bash
crewai train -n <n_iterations> <filename> (optional)
```

**Note: Replace <n_iterations> with the desired number of training iterations and <filename> with the appropriate filename ending with `.pkl`.**

### Training Your Crew Programmatically:

To train your crew programmatically, use the following steps:

- Define the number of iterations for training.
- Specify the input parameters for the training process.
- Execute the training command within a try-except block to handle potential errors.

```python
n_iterations = 2
inputs = {"topic": "CrewAI Training"}
filename = "your_model.pkl"

try:
    YourCrewName_Crew().crew().train(
      n_iterations=n_iterations,
      inputs=inputs,
      filename=filename
    )

except Exception as e:
    raise Exception(f"An error occurred while training the crew: {e}")
```

### Key Points to Note:

- **<filename>**: You provide the filename so CrewAI knows where to write the resulting model.
- **Positive Integer Requirement:** Ensure that the number of iterations (n_iterations) is a positive integer. The code will raise a ValueError if this condition is not met.
- **Filename Requirement:** Ensure that the filename ends with .pkl. The code will raise a ValueError if this condition is not met.
- Error Handling: The code handles subprocess errors and unexpected exceptions, providing error messages to the user.

It is important to note that the training process may take some time, depending on the complexity of your agents and will also require your feedback on each iteration.

Once the training is complete, your agents will be equipped with enhanced capabilities and knowledge, ready to tackle complex tasks and provide more consistent and valuable insights.

Remember to regularly update and retrain your agents to ensure they stay up-to-date with the latest information and advancements in the field.
