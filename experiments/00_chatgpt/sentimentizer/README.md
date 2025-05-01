# Sentimenter

Goals 
- Create a simple script to retrieve the sentiment of a AI prompt.
- Return in standardized Typescript.

## Example
```
$ py main.py
Device set to use mps:0
I hate tacos.
const response: SentimentResponse = {
  "polarity": -0.8,
  "subjectivity": 0.9,
  "emotion": [
    "disgust",
    "anger"
  ],
  "intensity": "moderate",
  "toxicity": true,
  "targeted_sentiment": {}
};


I fucking love tacos and hate eggplant.
const response: SentimentResponse = {
  "polarity": -0.15,
  "subjectivity": 0.75,
  "emotion": [
    "disgust",
    "anger"
  ],
  "intensity": "moderate",
  "toxicity": true,
  "targeted_sentiment": {}
};


Edamame is kinda gross.
const response: SentimentResponse = {
  "polarity": 0.0,
  "subjectivity": 0.0,
  "emotion": [
    "disgust"
  ],
  "intensity": "high",
  "toxicity": false,
  "targeted_sentiment": {}
};



$ 
```

## Sentiment Descriptions
```
type SentimentResponse = {
  polarity: number; // Sentiment strength from -1 (very negative) to 1 (very positive)
  subjectivity: number; // How subjective (1) or objective (0) the text is
  emotion: string[]; // Primary emotions detected, e.g., "joy", "anger"
  intensity: "low" | "moderate" | "high"; // Strength of emotional expression
  toxicity: boolean; // Whether toxic language is present
  targeted_sentiment: { [target: string]: number }; // Sentiment toward specific keywords/entities
};
```
