#!/usr/bin/env python3
"""
EXERCISE 1: The Simplest API Call Possible
Goal: Send "What is 2+2?" to AI and see what comes back

This version uses a FAKE API response so you can:
1. Run it without needing an API key yet
2. See exactly what the response structure looks like
3. Understand the flow before spending money
"""

import json

def fake_api_call(message):
    """
    Simulates what OpenAI's API returns
    This is EXACTLY the structure you get back (simplified)
    """
    
    print("🔄 SENDING TO API:")
    print(f"   Message: '{message}'")
    print()
    
    # This is what OpenAI actually sends back (simplified)
    fake_response = {
        "id": "chatcmpl-ABC123",
        "object": "chat.completion",
        "created": 1234567890,
        "model": "gpt-4o-mini",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "2 + 2 equals 4"
                },
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 6,
            "total_tokens": 16
        }
    }
    
    return fake_response

def main():
    print("=" * 50)
    print("EXERCISE 1: Basic API Call")
    print("=" * 50)
    print()
    
    # Step 1: The message we want to send
    my_message = "What is 2+2?"
    
    # Step 2: Call the API (fake for now)
    response = fake_api_call(my_message)
    
    # Step 3: Show the FULL response
    print("📥 FULL API RESPONSE:")
    print(json.dumps(response, indent=2))
    print()
    
    # Step 4: Extract just the answer
    print("🎯 EXTRACTED ANSWER:")
    answer = response["choices"][0]["message"]["content"]
    print(f"   {answer}")
    print()
    
    # Step 5: Show what we learned
    print("📊 WHAT WE LEARNED:")
    print(f"   - Response ID: {response['id']}")
    print(f"   - Model used: {response['model']}")
    print(f"   - Tokens used: {response['usage']['total_tokens']} (this costs money!)")
    print(f"   - Finish reason: {response['choices'][0]['finish_reason']}")

if __name__ == "__main__":
    main()