#!/usr/bin/env python3
"""
EXERCISE 1C: Foolproof API Call
This version handles API keys in multiple ways so it ALWAYS works
"""

import json
import os
import sys
from pathlib import Path

def get_api_key():
    """
    Gets API key using multiple methods
    Shows you EXACTLY what's happening so no confusion
    """
    print("🔍 Looking for API key...")
    
    # Method 1: Check environment variable
    from_env = os.getenv("OPENAI_API_KEY")
    if from_env:
        print("✅ Found API key in environment variable!")
        return from_env
    else:
        print("   No environment variable found")
    
    # Method 2: Check .env file
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        print(f"📄 Found .env file at: {env_file}")
        try:
            with open(env_file, 'r') as f:
                for line in f:
                    if line.startswith("OPENAI_API_KEY="):
                        key = line.split("=", 1)[1].strip()
                        # Remove quotes if present
                        key = key.strip('"').strip("'")
                        print("✅ Found API key in .env file!")
                        return key
            print("   .env file exists but no OPENAI_API_KEY found")
        except Exception as e:
            print(f"   Error reading .env: {e}")
    else:
        print(f"   No .env file found at {env_file}")
    
    # Method 3: Ask user
    print("\n❓ No API key found automatically.")
    print("   Get your key from: https://platform.openai.com/api-keys")
    key = input("   Paste your API key here (or 'skip' to exit): ").strip()
    
    if key.lower() == 'skip':
        return None
    
    # Offer to save it
    if key.startswith("sk-"):
        print("\n💾 Would you like to save this key for next time?")
        save = input("   Save to .env file? (yes/no): ").lower()
        if save == 'yes':
            with open(env_file, 'w') as f:
                f.write(f"OPENAI_API_KEY={key}\n")
            print(f"✅ Saved to {env_file}")
            print("   (Don't commit this file to Git!)")
    
    return key

def test_api_key(api_key):
    """
    Tests if the API key actually works
    """
    import requests
    
    print("\n🔬 Testing API key...")
    
    url = "https://api.openai.com/v1/models"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("✅ API key is valid!")
            return True
        elif response.status_code == 401:
            print("❌ API key is invalid (401 Unauthorized)")
            return False
        else:
            print(f"⚠️  Unexpected response: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False

def call_openai(api_key, message):
    """
    Calls OpenAI API with clear error messages
    """
    import requests
    
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": message}],
        "temperature": 0.7
    }
    
    print("\n📤 Calling OpenAI API...")
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ API Error {response.status_code}: {response.text}")
        return None

def main():
    print("=" * 60)
    print("FOOLPROOF API CALLING")
    print("=" * 60)
    print()
    
    # Get API key using foolproof method
    api_key = get_api_key()
    
    if not api_key:
        print("\n⏹️  Exiting without API key")
        return
    
    # Test the key
    if not test_api_key(api_key):
        print("\n⚠️  API key doesn't seem to work. Check:")
        print("   1. Is it active? Check: https://platform.openai.com/api-keys")
        print("   2. Do you have credits? Check: https://platform.openai.com/usage")
        return
    
    # Make a test call
    response = call_openai(api_key, "Say 'Hello, API is working!' in exactly those words")
    
    if response:
        print("\n✨ SUCCESS! Response from OpenAI:")
        print("-" * 40)
        answer = response["choices"][0]["message"]["content"]
        print(answer)
        print("-" * 40)
        
        # Show token usage
        tokens = response["usage"]["total_tokens"]
        cost = tokens * 0.00000015
        print(f"\n📊 Used {tokens} tokens (cost: ${cost:.6f})")

if __name__ == "__main__":
    main()