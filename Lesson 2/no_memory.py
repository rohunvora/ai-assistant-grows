#!/usr/bin/env python3
"""
DEMO: AI With NO MEMORY
This shows why AI seems "dumb" - it forgets everything!
"""

import requests

# Read API key
with open('.env', 'r') as f:
    line = f.read().strip()
    api_key = line.split('OPENAI_API_KEY=')[1].strip()

def ask_ai(message):
    """Send a single message to AI (no history)"""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": message}]
    }
    
    print("📤 SENDING TO AI:")
    print(f"   Just this message: '{message}'")
    print(f"   (No previous conversation included)")
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    return "Error"

# Test conversation WITHOUT memory
print("="*60)
print("CHAT WITH NO MEMORY (Like Lesson 1)")
print("="*60)
print("\nLet's have a conversation...\n")

# Message 1
print("You: My name is Bob")
response1 = ask_ai("My name is Bob")
print(f"AI: {response1}")

print("\n" + "-"*60 + "\n")

# Message 2 - AI won't remember!
print("You: What's my name?")
response2 = ask_ai("What's my name?")
print(f"AI: {response2}")

print("\n" + "="*60)
print("❌ SEE THE PROBLEM?")
print("The AI forgot your name because we only sent")
print("'What's my name?' without the previous conversation!")
print("="*60)