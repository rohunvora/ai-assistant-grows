#!/usr/bin/env python3
"""
SUPER SIMPLE API KEY TEST
Just checks if your key works - nothing fancy
"""

print("=" * 50)
print("TESTING YOUR API KEY")
print("=" * 50)
print()

# Step 1: Read your .env file
print("📂 Reading .env file...")
try:
    with open('.env', 'r') as f:
        line = f.read().strip()
        if 'OPENAI_API_KEY=' in line:
            api_key = line.split('OPENAI_API_KEY=')[1].strip()
            print(f"✅ Found key: {api_key[:7]}...")  # Show first 7 chars only
        else:
            print("❌ .env file doesn't have OPENAI_API_KEY=")
            print("   Make sure the file has: OPENAI_API_KEY=your-actual-key")
            exit()
except FileNotFoundError:
    print("❌ No .env file found!")
    print("   Create a file called .env with: OPENAI_API_KEY=your-key")
    exit()

# Step 2: Check if it looks like a real key
print()
print("🔍 Checking key format...")
if not api_key.startswith('sk-'):
    print("❌ Key doesn't start with 'sk-'")
    print("   OpenAI keys always start with 'sk-'")
    exit()
else:
    print("✅ Key format looks correct")

# Step 3: Test with OpenAI
print()
print("🌐 Testing with OpenAI API...")
import requests

url = "https://api.openai.com/v1/models"
headers = {"Authorization": f"Bearer {api_key}"}

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("✅ SUCCESS! Your API key works!")
        print()
        print("🎉 You're ready to make AI calls!")
    elif response.status_code == 401:
        print("❌ API key is invalid")
        print("   Double-check you copied the entire key")
        print("   Keys look like: sk-proj-veryLongStringOfCharacters")
    else:
        print(f"⚠️ Unexpected response: {response.status_code}")
        print("   This might be a temporary issue")
except Exception as e:
    print(f"❌ Connection error: {e}")
    print("   Check your internet connection")

print()
print("=" * 50)