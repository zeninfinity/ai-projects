from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "gpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = input("Enter a prompt: ")
inputs = tokenizer(prompt, return_tensors="pt")

output = model.generate(
    **inputs,
    max_length=100,
    temperature=0.9,
    top_k=50,
    top_p=0.95,
    repetition_penalty=1.2,
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id
)

print(tokenizer.decode(output[0], skip_special_tokens=True))
