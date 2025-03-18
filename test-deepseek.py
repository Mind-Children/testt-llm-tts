from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-r1")
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-r1")

prompt = "Hello, Deepseek R1!"

inputs = tokenizer(prompt,return_tensors="pt")
outputs = model.generate(**inputs,max_length=50)

print(tokenizer.decode(outputs[0],skip_special_tokens=True))
