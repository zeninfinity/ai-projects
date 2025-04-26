from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

# model_name = "EleutherAI/gpt-neo-1.3B" # 1.9GB
# model_name = "tiiuae/falcon-rw-1b" # 2.3GB

#model_name = "gpt2"
#AutoModelForCausalLM.from_pretrained(model_name, cache_dir="./model")
#AutoTokenizer.from_pretrained(model_name, cache_dir="./model")

model_name = "EleutherAI/gpt-neo-1.3B"
model_dir = "./model"
# Download model if not already cached
if not os.path.isdir(model_dir) or not os.listdir(model_dir):
    print("Model not found. Downloading...")
    AutoModelForCausalLM.from_pretrained(model_name, cache_dir=model_dir)
    AutoTokenizer.from_pretrained(model_name, cache_dir=model_dir)
    print("Download complete.")

# Load from local cache
model = AutoModelForCausalLM.from_pretrained(model_dir)
tokenizer = AutoTokenizer.from_pretrained(model_dir)

# Prompt and generate
prompt = input("Enter a prompt: ")
inputs = tokenizer(prompt, return_tensors="pt")

output = model.generate(
    **inputs,
    max_length=60,
    temperature=0.7,
    top_k=40,
    top_p=0.9,
    repetition_penalty=1.3,
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id
)

print("\n" + tokenizer.decode(output[0], skip_special_tokens=True))
