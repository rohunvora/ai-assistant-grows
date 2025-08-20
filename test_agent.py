#!/usr/bin/env python3
"""Test the agent with predefined inputs to see loop prevention"""

from simple_agent import VisibleAgent

print("TESTING AGENT LOOP PREVENTION")
print("=" * 50)

agent = VisibleAgent(debug=True)

# Test 1: Normal conversation
print("\n--- Test 1: Normal Conversation ---")
print(f"Response: {agent.process_message('Hello')}")
print(f"Response: {agent.process_message('What is the weather?')}")

# Test 2: Loop prevention
print("\n--- Test 2: Loop Prevention (same message 4 times) ---")
for i in range(4):
    print(f"\nAttempt {i+1}:")
    response = agent.process_message("Calculate something")
    print(f"Response: {response}")

# Test 3: Reset and try again
print("\n--- Test 3: After Reset ---")
agent.reset()
print(f"Response: {agent.process_message('Calculate something')}")