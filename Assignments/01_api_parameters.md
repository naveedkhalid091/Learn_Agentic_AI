## Paramters: 

### Messages:  
  * **Purpose:** The **purpose** of this parameter is to structure the conversation between the users and the AI. 
  * **Functionality**: It provides a list of message objects, where each object contains a role and content.

### Model: 
 * **Purpose:** This parameter allow us to select the different available models, it is like a brain of AI.  
 * **Functionality:** You select the model based on your requirements for accuracy, speed or cost.

### Max Completion Token: 
 * **Purpose**: This parameter limits the number of tokens that AI can generate in its response.
 * A token is a piece of text that helps to control the lenght of the output and manage the costs since pricing is token based. 
 * For Example: if `max-token` is set to 100, the response will not exceed 100 tokens.

### n: 
* This parameter specifies the AI how many responses you need to generate in a single output.
* For Example: n:2 will generate 2 different completions/outputs.

### Stream: 
* The purpose of this parameter is to deliver the response in a real time, rather then showing all the completed output at once.
* When stream is set to "true", the responses are sent increamentally.

### Temperature: 
* This parameter controls the creativity or randomness in AI responses.
* Its value falls in between 0 to 1, higher the number creates a more creative response while lower number like 0 or 0.2 generates are lower creative output.

### Top-p: 

* This a another way to control the creativity, you can use as an alternative to the `temperature` parameter. 
* For Example: setting Top_p=0.9 means AI only considers the top 90% of the answer.

### Tools: 
* Tools are the extra features in AI that can use to help with specific tasks, like browsing the internet, generating images or running code.
* Tools might include access to a database or APIs for specific applications.
