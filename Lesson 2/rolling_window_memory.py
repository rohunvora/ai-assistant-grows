#!/usr/bin/env python3
"""
ROLLING WINDOW MEMORY
Only keeps last N messages to avoid token limits
"""

import requests

# Read API key
with open('.env', 'r') as f:
    line = f.read().strip()
    api_key = line.split('OPENAI_API_KEY=')[1].strip()

# CONFIGURATION
MAX_MESSAGES = 6  # Only keep last 6 messages (3 exchanges)
conversation = []
total_messages_sent = 0

def show_memory_status():
    """Show what's in memory vs what's been dropped"""
    print("\n📊 MEMORY STATUS:")
    print(f"   Total messages sent: {total_messages_sent}")
    print(f"   Messages in memory: {len(conversation)}")
    print(f"   Messages dropped: {max(0, total_messages_sent - len(conversation))}")
    
    if len(conversation) > 0:
        print("\n📦 CURRENT MEMORY WINDOW:")
        print("   ┌" + "─"*45 + "┐")
        for msg in conversation:
            text = f"{msg['role']}: {msg['content']}"[:43]
            print(f"   │ {text.ljust(43)} │")
        print("   └" + "─"*45 + "┘")

def chat_with_rolling_window(message):
    """Chat with limited memory"""
    global total_messages_sent
    
    # Add user message
    conversation.append({"role": "user", "content": message})
    total_messages_sent += 1
    
    # IMPORTANT: Trim to max size BEFORE sending
    if len(conversation) > MAX_MESSAGES:
        dropped = len(conversation) - MAX_MESSAGES
        conversation[:] = conversation[-MAX_MESSAGES:]  # Keep only last N
        print(f"\n⚠️  Dropped {dropped} old messages to stay under limit!")
    
    # Show what we're sending
    show_memory_status()
    
    # Call API with limited history
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": conversation
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        ai_response = result["choices"][0]["message"]["content"]
        tokens = result["usage"]["total_tokens"]
        
        # Add AI response
        conversation.append({"role": "assistant", "content": ai_response})
        total_messages_sent += 1
        
        print(f"\n🤖 AI: {ai_response}")
        print(f"💰 Tokens: {tokens} (stays low because we limit history!)")

# Demo
print("="*60)
print("ROLLING WINDOW MEMORY DEMO")
print(f"Maximum messages kept: {MAX_MESSAGES}")
print("="*60)
print("\nWatch what happens as we chat...\n")

# Have a conversation that will exceed the limit
test_messages = [
    "My name is Bob",
    "I live in New York",
    "My favorite color is blue",
    "I have a dog named Max",
    "What's my name?",  # This should still work
    "What's my dog's name?",  # This might forget
    "What's my favorite color?"  # This will definitely forget
]

for i, msg in enumerate(test_messages, 1):
    print(f"\n{'='*60}")
    print(f"MESSAGE #{i}: \"{msg}\"")
    print('='*60)
    chat_with_rolling_window(msg)
    
    if i == 4:
        print("\n🔔 NOTE: We're at the memory limit. Next message will drop old ones!")

print("\n" + "="*60)
print("💡 WHAT HAPPENED?")
print("="*60)
print("The AI forgot your name and favorite color because")
print("those messages were dropped from the memory window!")
print("\nThis is why choosing the right memory method matters.")
print("="*60)