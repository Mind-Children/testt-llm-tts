from ollama import chat

#LLM_MODEL = 'gemma2:2b'
#LLM_MODEL = 'qwen2.5:0.5b'
#LLM_MODEL = 'qwen2.5:1.5b'
LLM_MODEL = 'qwen2.5:3b'
#LLM_MODEL = 'tinyllama:1.1b'

class LLM:

    def __init__(self):
        self.complete("how is the weather?","You are a weather reporter.")

    def complete(self,prompt,system_prompt):
        response = chat(LLM_MODEL,messages=[{'role':'system','content':system_prompt},{'role':'user','content':prompt}])
        return response['message']['content']
