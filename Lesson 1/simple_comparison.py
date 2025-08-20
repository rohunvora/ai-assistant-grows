#!/usr/bin/env python3
"""
SIMPLE MODEL COMPARISON - GPT-4o-mini vs GPT-4o
See the difference clearly!
"""

import requests
import time

# Read API key
with open('.env', 'r') as f:
    line = f.read().strip()
    api_key = line.split('OPENAI_API_KEY=')[1].strip()

def call_model(model_id, message):
    """Call a specific model"""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model_id,
        "messages": [{"role": "user", "content": message}],
        "temperature": 0.7,
        "max_tokens": 250
    }
    
    start = time.time()
    response = requests.post(url, headers=headers, json=data)
    elapsed = time.time() - start
    
    if response.status_code == 200:
        result = response.json()
        return {
            "response": result["choices"][0]["message"]["content"],
            "tokens": result["usage"]["total_tokens"],
            "time": elapsed
        }
    return None

def compare(question):
    """Compare both models side by side"""
    print("\n" + "="*70)
    print(f"QUESTION: {question}")
    print("="*70)
    
    # Test cheap model
    print("\n🟢 GPT-4o-MINI (CHEAP - $0.15 per 1M tokens)")
    print("-"*70)
    mini_result = call_model("gpt-4o-mini", question)
    if mini_result:
        print(mini_result["response"])
        print("-"*70)
        mini_cost = (mini_result["tokens"] / 1_000_000) * 0.15
        print(f"⏱️  Time: {mini_result['time']:.2f}s | 🪙 Cost: ${mini_cost:.8f}")
    
    # Test expensive model
    print("\n🔴 GPT-4o (EXPENSIVE - $5.00 per 1M tokens)")
    print("-"*70)
    gpt4_result = call_model("gpt-4o", question)
    if gpt4_result:
        print(gpt4_result["response"])
        print("-"*70)
        gpt4_cost = (gpt4_result["tokens"] / 1_000_000) * 5.00
        print(f"⏱️  Time: {gpt4_result['time']:.2f}s | 🪙 Cost: ${gpt4_cost:.8f}")
    
    # Show cost difference
    if mini_result and gpt4_result:
        ratio = gpt4_cost / mini_cost
        print(f"\n💰 COST DIFFERENCE: GPT-4o is {ratio:.1f}x more expensive!")
        print(f"   You paid ${gpt4_cost:.8f} vs ${mini_cost:.8f}")

# Test prompts to try
print("="*70)
print("MODEL COMPARISON: GPT-4o-mini vs GPT-4o")
print("="*70)

print("\n🎯 SUGGESTED TEST PROMPTS:")
print("\n--- Simple (both should be similar) ---")
print("1. What is the capital of France?")
print("2. Convert 100 fahrenheit to celsius")

print("\n--- Creative (might see small differences) ---")
print("3. Write a 3-line poem about debugging code")
print("4. Explain why pizza is round but comes in square boxes")

print("\n--- Complex (might see bigger differences) ---")
print("5. Explain the difference between async and sync in programming")
print("6. What's wrong with this: if x = 5: print('hello')")

print("\n--- Reasoning (GPT-4o might excel) ---")
print("7. I have 3 apples. I eat 2, buy 5 more, give away half. How many left?")
print("8. Which is heavier: a pound of feathers or a pound of steel? Explain the trick.")

print("\n" + "-"*70)
print("Enter a number (1-8) or type your own question")
print("Type 'quit' to exit")
print("-"*70)

prompts = [
    "What is the capital of France?",
    "Convert 100 fahrenheit to celsius",
    "Write a 3-line poem about debugging code", 
    "Explain why pizza is round but comes in square boxes",
    "Explain the difference between async and sync in programming",
    "What's wrong with this: if x = 5: print('hello')",
    "I have 3 apples. I eat 2, buy 5 more, give away half. How many left?",
    "Which is heavier: a pound of feathers or a pound of steel? Explain the trick."
]

while True:
    choice = input("\n❓ Your choice: ").strip()
    
    if choice.lower() == 'quit':
        break
    
    if choice.isdigit() and 1 <= int(choice) <= 8:
        question = prompts[int(choice) - 1]
    else:
        question = choice
    
    compare(question)
    print("\n" + "="*70)
    print("Try another question to see more differences!")