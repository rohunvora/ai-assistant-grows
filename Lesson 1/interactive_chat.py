#!/usr/bin/env python3
"""
INTERACTIVE CHAT - Talk to AI yourself!
Type 'quit' to exit
"""

import requests

# Read API key
with open('.env', 'r') as f:
    line = f.read().strip()
    api_key = line.split('OPENAI_API_KEY=')[1].strip()

def call_ai(message):
    """Send message to AI and return response"""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": message}]
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"], result["usage"]["total_tokens"]
    else:
        return f"Error: {response.status_code}", 0

print("=" * 50)
print("INTERACTIVE AI CHAT")
print("Type your message and press Enter")
print("Type 'quit' to exit")
print("=" * 50)
print()

total_tokens = 0
total_cost = 0

while True:
    # Get user input
    user_input = input("You: ").strip()
    
    if user_input.lower() == 'quit':
        break
    
    # Call AI
    response, tokens = call_ai(user_input)
    
    # Show response
    print(f"AI: {response}")
    
    # Track usage
    total_tokens += tokens
    cost = tokens * 0.00000015
    total_cost += cost
    print(f"    (Used {tokens} tokens, cost: ${cost:.8f})")
    print()

print()
print("=" * 50)
print(f"Session totals: {total_tokens} tokens, ${total_cost:.6f}")
print("=" * 50)