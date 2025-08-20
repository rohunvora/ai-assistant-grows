#!/usr/bin/env python3
"""
YOUR FIRST REAL AI CALL
This will actually talk to OpenAI and cost about $0.00002
"""

import requests

print("=" * 50)
print("MY FIRST REAL AI CALL")
print("=" * 50)
print()

# Read your API key from .env
with open('.env', 'r') as f:
    line = f.read().strip()
    api_key = line.split('OPENAI_API_KEY=')[1].strip()

# The message we'll send
message = "What is 2+2? Reply in exactly 3 words."

print(f"📤 Sending: '{message}'")
print()

# Prepare the API call
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
data = {
    "model": "gpt-4o-mini",  # Cheapest model
    "messages": [
        {"role": "user", "content": message}
    ]
}

# Make the call
print("⏳ Calling OpenAI...")
response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    # Success! Parse the response
    result = response.json()
    
    # Extract the answer
    answer = result["choices"][0]["message"]["content"]
    
    print()
    print("🤖 AI Response:")
    print(f"   '{answer}'")
    print()
    
    # Show some interesting details
    print("📊 Behind the scenes:")
    print(f"   Model used: {result['model']}")
    print(f"   Tokens used: {result['usage']['total_tokens']}")
    cost = result['usage']['total_tokens'] * 0.00000015
    print(f"   Cost: ${cost:.8f} (less than a penny!)")
    print(f"   Response ID: {result['id']}")
    
else:
    print(f"❌ Error: {response.status_code}")
    print(response.text)

print()
print("=" * 50)