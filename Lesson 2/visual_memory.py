#!/usr/bin/env python3
"""
VISUAL MEMORY DEMO
See exactly what's happening with pictures!
"""

import requests
import time

# Read API key
with open('.env', 'r') as f:
    line = f.read().strip()
    api_key = line.split('OPENAI_API_KEY=')[1].strip()

def show_visual(message_num, history, new_message):
    """Draw a visual of what we're sending"""
    print("\n" + "="*60)
    print(f"MESSAGE #{message_num}")
    print("="*60)
    
    print("\n📝 YOU TYPE: \"" + new_message + "\"")
    
    print("\n📦 WHAT WE ACTUALLY SEND TO THE AI:")
    print("┌" + "─"*50 + "┐")
    
    if len(history) == 0:
        print("│ 1. " + new_message.ljust(46) + "│")
    else:
        for i, msg in enumerate(history, 1):
            if msg['role'] == 'user':
                print(f"│ {i}. YOU: {msg['content'][:40].ljust(40)} │")
            else:
                print(f"│ {i}. AI:  {msg['content'][:40].ljust(40)} │")
        print(f"│ {len(history)+1}. YOU: {new_message[:40].ljust(40)} │")
    
    print("└" + "─"*50 + "┘")

def chat_with_visual(message, history):
    """Send message and update history"""
    # Add new message
    history.append({"role": "user", "content": message})
    
    # Call API
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": history
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        ai_response = result["choices"][0]["message"]["content"]
        tokens = result["usage"]["total_tokens"]
        
        # Add AI response
        history.append({"role": "assistant", "content": ai_response})
        
        print("\n🤖 AI RESPONDS: \"" + ai_response + "\"")
        print(f"\n💰 COST: {tokens} tokens = ${tokens * 0.00000015:.8f}")
        
        return history
    return history

# Demo conversation
print("="*60)
print("VISUAL MEMORY DEMONSTRATION")
print("="*60)
print("\nWatch how the message box grows each time!")

conversation = []

# Message 1
show_visual(1, conversation, "My name is Bob")
conversation = chat_with_visual("My name is Bob", conversation)
time.sleep(1)

# Message 2
show_visual(2, conversation, "What's my name?")
conversation = chat_with_visual("What's my name?", conversation)
time.sleep(1)

# Message 3
show_visual(3, conversation, "Count to 3")
conversation = chat_with_visual("Count to 3", conversation)

print("\n" + "="*60)
print("💡 KEY INSIGHT:")
print("="*60)
print("Each new message includes ALL previous messages!")
print("That's why:")
print("- Message 1: Sent 1 thing")
print("- Message 2: Sent 3 things (growing!)")
print("- Message 3: Sent 5 things (keeps growing!)")
print("\nThis is how AI 'remembers' - you remind it every time!")
print("="*60)