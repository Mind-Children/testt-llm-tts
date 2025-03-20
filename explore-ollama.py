from ollama import chat

#model = 'deepseek-r1:1.5b'
#model = 'tinyllama:1.1b'
#model = 'llama3:8b'
#model = 'gemma3:1b'
#model = 'gemma3:4b'
model = 'qwen2.5:0.5b'

prompt = "Hello, chatbot. Please briefly explain how quantum mechanics works."

response = chat(model,messages=[{'role':'user','content':prompt}])

print(response)