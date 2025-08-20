#!/usr/bin/env python3
"""
EXERCISE 1B: Real API Call to OpenAI
This time we'll actually call OpenAI's API

SETUP REQUIRED:
1. Get API key from: https://platform.openai.com/api-keys
2. Add credit card (minimum $5): https://platform.openai.com/settings/billing
3. Put your API key in the code below (we'll make it secure later)
"""

import json
import requests

# PUT YOUR API KEY HERE (we'll make this secure in a later lesson)
# Get it from: https://platform.openai.com/api-keys
API_KEY = "sk-..."  # <-- Replace with your actual key

def call_openai_api(message):
    """
    Actually calls OpenAI's API
    This is the REAL thing - it will cost money (about $0.00002)
    """
    
    # The API endpoint
    url = "https://api.openai.com/v1/chat/completions"
    
    # Headers (including your API key)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    # The data we're sending
    data = {
        "model": "gpt-4o-mini",  # Cheapest model
        "messages": [
            {"role": "user", "content": message}
        ],
        "temperature": 0.7
    }
    
    print("🔄 SENDING TO OPENAI:")
    print(f"   URL: {url}")
    print(f"   Model: {data['model']}")
    print(f"   Message: '{message}'")
    print()
    
    try:
        # Make the actual API call
        response = requests.post(url, headers=headers, json=data)
        
        # Check if it worked
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ API Error: {response.status_code}")
            print(f"   Message: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return None

def main():
    print("=" * 50)
    print("EXERCISE 1B: Real OpenAI API Call")
    print("=" * 50)
    print()
    
    # Check if API key is set
    if API_KEY == "sk-...":
        print("⚠️  You need to add your OpenAI API key first!")
        print("   1. Get it from: https://platform.openai.com/api-keys")
        print("   2. Replace 'sk-...' in this file with your actual key")
        print("   3. Run this script again")
        print()
        print("Don't have an API key? No problem!")
        print("Keep using exercise1_basic_call.py with fake responses for now.")
        return
    
    # The message we want to send
    my_message = "What is 2+2?"
    
    # Call the REAL API
    response = call_openai_api(my_message)
    
    if response:
        # Show the FULL response
        print("📥 FULL API RESPONSE:")
        print(json.dumps(response, indent=2))
        print()
        
        # Extract just the answer
        print("🎯 THE ANSWER:")
        answer = response["choices"][0]["message"]["content"]
        print(f"   {answer}")
        print()
        
        # Show cost info
        tokens = response["usage"]["total_tokens"]
        cost = tokens * 0.00000015  # Approximate cost for gpt-4o-mini
        print("💰 COST INFO:")
        print(f"   Tokens used: {tokens}")
        print(f"   Approximate cost: ${cost:.6f}")

if __name__ == "__main__":
    main()