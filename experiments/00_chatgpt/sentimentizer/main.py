from modules.sentiment import Sentiment

with open('prompts', 'r') as file:
    sentences = [line.strip() for line in file.readlines()]

for s in sentences:
    print(s)
    print(Sentiment(s))
    print("\n")
