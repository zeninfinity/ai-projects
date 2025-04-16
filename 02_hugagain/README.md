Here’s the step-by-step guide to get Docker working with a model that you can interact with via the terminal. No fluff — just the essentials.

⸻

1. Install Docker

If you haven’t already, make sure Docker is installed on your machine.
	•	MacOS: Download Docker Desktop
	•	Linux: Follow the instructions for your distro from Docker’s website
	•	Windows: Download Docker Desktop

2. Create a Project Folder
	•	Create a new directory for your project, e.g., ai-docker.

mkdir ai-docker
cd ai-docker

3. Dockerfile
	•	Create a Dockerfile to set up the environment.
	•	Inside ai-docker/ folder, create the Dockerfile:

# Use official Python image as base
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy your code
COPY . /app

# Command to run the app
CMD ["python", "run_model.py"]

4. Requirements File
	•	Create a requirements.txt in the same directory with these contents:

transformers==4.26.1
torch==1.13.1

5. Python Script for Terminal Interaction
	•	Create a run_model.py script that loads a pre-trained model and interacts with it from the terminal. Here’s an example:

from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
model_name = "gpt2"  # You can change this to any model on Hugging Face
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Function to generate text
def generate_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))

if __name__ == "__main__":
    while True:
        prompt = input("Enter a prompt: ")
        generate_text(prompt)

This script:
	•	Loads GPT-2 (or another model) from Hugging Face
	•	Continuously prompts the user for input, generates a response, and prints it to the terminal.

6. Build the Docker Image
	•	In the terminal, in the project folder (ai-docker), run:

docker build -t ai-gpt2 .

This will:
	•	Build the Docker image based on the Dockerfile
	•	Pull Python, install dependencies, and copy your code

7. Run the Docker Container
	•	Once the build finishes, run the container with:

docker run --rm ai-gpt2

	•	This will start the model in the terminal and let you enter prompts.
	•	If everything works, you’ll see a prompt asking you to enter text, and the model will generate responses.

8. (Optional) Handle GPU Support
	•	If you have a GPU and want to use it with Docker, ensure you have the NVIDIA Docker toolkit installed and use the --gpus flag.
	•	You can follow NVIDIA’s Docker GPU instructions for setup.

⸻

Troubleshooting
	•	Slow downloads: The first time you pull a model, it can take a while. If it stalls, check your internet connection or try pulling the model outside of Docker first.
	•	Memory issues: Models like GPT-2 are large. If you run into memory problems, try smaller models like distilgpt2.

⸻

Next Steps

Once this is working, you can:
	1.	Change the model in run_model.py for different capabilities (e.g., EleutherAI/gpt-neo-1.3B for more power).
	2.	Experiment with different prompts and see how the model responds.
	3.	Add advanced features like logging or batch processing.

This setup will give you a working, terminal-based AI environment within Docker that you can expand on. Let me know if you hit any issues along the way.

--
On Host Machine - python3 -c "from transformers import AutoModelForCausalLM, AutoTokenizer; AutoModelForCausalLM.from_pretrained('gpt2'); AutoTokenizer.from_pretrained('gpt2')"

Then Mount on docker - docker run --rm -v $HOME/.cache/huggingface:/root/.cache/huggingface ai-gpt2

Update model info:
```
print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(model_name)
print("Model loaded.")

```

Lighter Model - model_name = "distilgpt2"
