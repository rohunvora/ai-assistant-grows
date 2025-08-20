#!/usr/bin/env python3
"""
DEMO: AI WITH MEMORY
Now the AI remembers because we send the history!
"""

import requests

# Read API key
with open('.env', 'r') as f:
    line = f.read().strip()
    api_key = line.split('OPENAI_API_KEY=')[1].strip()

# THIS IS THE KEY: We store the conversation!
conversation_history = []

def ask_ai_with_memory(message):
    """Send message WITH conversation history"""
    
    # Add user's message to history
    conversation_history.append({"role": "user", "content": message})
    
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": conversation_history  # Send ALL messages!
    }
    
    print("📤 SENDING TO AI:")
    print(f"   Current message: '{message}'")
    print(f"   Plus {len(conversation_history)-1} previous messages")
    print(f"   Total messages sent: {len(conversation_history)}")
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        ai_response = result["choices"][0]["message"]["content"]
        
        # IMPORTANT: Add AI's response to history too!
        conversation_history.append({"role": "assistant", "content": ai_response})
        
        return ai_response
    return "Error"

# Test conversation WITH memory
print("="*60)
print("CHAT WITH MEMORY (What we're building!)")
print("="*60)
print("\nLet's have the same conversation...\n")

# Message 1
print("You: My name is Bob")
response1 = ask_ai_with_memory("My name is Bob")
print(f"AI: {response1}")

print("\n" + "-"*60 + "\n")

# Message 2 - AI WILL remember!
print("You: What's my name?")
response2 = ask_ai_with_memory("What's my name?")
print(f"AI: {response2}")

print("\n" + "="*60)
print("✅ IT REMEMBERS!")
print("Because we sent BOTH messages to the AI:")
print("1. 'My name is Bob'")
print("2. AI's response")
print("3. 'What's my name?'")
print("="*60)