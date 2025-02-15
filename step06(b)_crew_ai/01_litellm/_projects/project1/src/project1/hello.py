from litellm import completion

import os

os.environ['GEMINI_API_KEY'] = "AIzaSyAR3gJ_0uvCYVwK1FOQPYyAewHJQ-hUaxY"

def call_gemini():
    response = completion(
    model="gemini/gemini-1.5-flash", 
    messages=[{"role": "user", "content": "Who is Quaid e Azam"}]
    )
    print(response['choices'][0]['message']['content']) # this method is provided in liteLLM docs. 

# Changing model in a same code:  

def call_gemini2():
    response = completion(
    model="gemini/gemini-2.0-flash-exp", 
    messages=[{"role": "user", "content": "Who is the founder of PIAIC?"}]
    )
    print(response['choices'][0]['message']['content']) # this method is provided in liteLLM docs. 
