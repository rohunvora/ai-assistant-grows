#!/usr/bin/env python3
"""
SUPER SIMPLE MODEL COMPARISON
Just type your question and see both responses
"""

import requests

# Read API key
with open('.env', 'r') as f:
    line = f.read().strip()
    api_key = line.split('OPENAI_API_KEY=')[1].strip()

# CHANGE THESE TWO LINES TO COMPARE DIFFERENT MODELS
MODEL_1 = "gpt-4.1"    # First model to test
MODEL_2 = "gpt-5"         # Second model to test

def ask_ai(model, question):
    """Ask a question to a specific model"""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": question}]
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    return "Error getting response"

# Main program
print("="*60)
print("MODEL COMPARISON")
print(f"Comparing: {MODEL_1} vs {MODEL_2}")
print("="*60)
print("\nType your question (or 'quit' to exit)")

while True:
    print()
    question = input("Your question: ").strip()
    
    if question.lower() == 'quit':
        break
    
    # Get response from first model
    print(f"\n--- {MODEL_1} ---")
    response1 = ask_ai(MODEL_1, question)
    print(response1)
    
    # Get response from second model
    print(f"\n--- {MODEL_2} ---")
    response2 = ask_ai(MODEL_2, question)
    print(response2)
    
    print("\n" + "="*60)