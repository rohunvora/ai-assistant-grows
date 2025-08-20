#!/usr/bin/env python3
"""
SEE THE MEMORY: Shows exactly what we send each time
This makes it crystal clear how "memory" works
"""

import requests
import json

# Read API key
with open('.env', 'r') as f:
    line = f.read().strip()
    api_key = line.split('OPENAI_API_KEY=')[1].strip()

conversation_history = []

def ask_ai_and_show_everything(message):
    """Ask AI and show EXACTLY what we're sending"""
    
    # Add user message to history
    conversation_history.append({"role": "user", "content": message})
    
    # Show what we're sending
    print("\n📦 FULL MESSAGE TO AI:")
    print("-" * 40)
    for i, msg in enumerate(conversation_history, 1):
        print(f"{i}. {msg['role']}: {msg['content']}")
    print("-" * 40)
    
    # Make API call
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": conversation_history
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        ai_response = result["choices"][0]["message"]["content"]
        tokens = result["usage"]["total_tokens"]
        
        # Add AI response to history
        conversation_history.append({"role": "assistant", "content": ai_response})
        
        print(f"\n🤖 AI RESPONSE: {ai_response}")
        print(f"💰 Tokens used: {tokens} (cost: ${tokens * 0.00000015:.8f})")
        
        return ai_response
    return "Error"

# Interactive chat
print("="*60)
print("SEE THE MEMORY - Watch what we send each time")
print("="*60)
print("\nType messages and watch the history grow!")
print("Try: 'My name is Bob', then 'What's my name?'")
print("Type 'quit' to exit\n")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == 'quit':
        break
    
    ask_ai_and_show_everything(user_input)
    print("\n" + "="*60)