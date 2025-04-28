import random

# List of rotating journal prompts
prompts = [
    "Reflect on your focus: What went well?",
    "What challenged you today and how did you overcome it?",
    "What is one thing you are proud of from this session?",
    "What distracted you today and how can you handle it next time?",
    "How do you feel about your progress today?",
    "What positive habits are you building?",
    "How did you stay mindful during this session?",
    "List one thing you’re grateful for right now.",
    "What self-care act can you reward yourself with after today’s work?"
]

def get_random_prompt():
    return random.choice(prompts)
