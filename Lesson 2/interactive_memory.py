#!/usr/bin/env python3
"""
INTERACTIVE MEMORY CHAT
Type messages and watch the memory box grow!
"""

import requests

# Read API key
with open('.env', 'r') as f:
    line = f.read().strip()
    api_key = line.split('OPENAI_API_KEY=')[1].strip()

conversation = []
message_count = 0

def show_memory_box():
    """Show what we're sending"""
    print("\n📦 MEMORY BOX (What we send to AI):")
    print("┌" + "─"*50 + "┐")
    if len(conversation) == 0:
        print("│ (empty - first message)                         │")
    else:
        for i, msg in enumerate(conversation, 1):
            if msg['role'] == 'user':
                text = f"{i}. YOU: {msg['content']}"[:46]
                print(f"│ {text.ljust(48)} │")
            else:
                text = f"{i}. AI: {msg['content']}"[:46]
                print(f"│ {text.ljust(48)} │")
    print("└" + "─"*50 + "┘")

def chat(message):
    """Send message with history"""
    global message_count
    message_count += 1
    
    # Show what we're about to send
    print(f"\n{'='*60}")
    print(f"MESSAGE #{message_count}")
    print('='*60)
    
    show_memory_box()
    print(f"\n➕ ADDING YOUR NEW MESSAGE: \"{message}\"")
    
    # Add to conversation
    conversation.append({"role": "user", "content": message})
    
    # Call API
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
        
        # Add AI response to history
        conversation.append({"role": "assistant", "content": ai_response})
        
        print(f"\n🤖 AI: {ai_response}")
        print(f"\n📊 Memory box now has {len(conversation)} messages")
        print(f"💰 Used {tokens} tokens (${tokens * 0.00000015:.8f})")

# Start chat
print("="*60)
print("INTERACTIVE MEMORY CHAT")
print("="*60)
print("\n🎮 INSTRUCTIONS:")
print("- Type messages and watch the memory box grow")
print("- Try: 'My name is Bob' then 'What's my name?'")
print("- Type 'clear' to start fresh")
print("- Type 'quit' to exit")
print()

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == 'quit':
        break
    elif user_input.lower() == 'clear':
        conversation = []
        message_count = 0
        print("\n🗑️ Memory cleared! Starting fresh.")
        continue
    
    chat(user_input)