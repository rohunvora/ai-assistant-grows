#!/usr/bin/env python3
"""
SIMPLE AGENT - Learning Version
This shows EVERYTHING that happens so you can understand the flow
"""

import os
import json
from typing import Dict, List, Optional

# CONFIGURATION - Everything in one place, visible
class Config:
    # You can hardcode for learning (remove before sharing!)
    API_KEY = "your-openai-api-key-here"  # Get from platform.openai.com
    MODEL = "gpt-4o-mini"  # Cheap and fast
    MAX_ATTEMPTS = 3  # Prevent infinite loops
    
    # Or load from environment (more secure)
    @classmethod
    def load_from_env(cls):
        cls.API_KEY = os.getenv("OPENAI_API_KEY", cls.API_KEY)

class VisibleAgent:
    """An agent that shows you everything it's doing"""
    
    def __init__(self, debug=True):
        self.debug = debug
        self.conversation_history = []
        self.attempt_counter = {}  # Track what we've tried
        self.state = "ready"
        
    def show_debug(self, message: str, data: any = None):
        """Show what's happening inside the agent"""
        if self.debug:
            print(f"\n🔍 DEBUG: {message}")
            if data:
                print(f"   Data: {json.dumps(data, indent=2) if isinstance(data, dict) else data}")
    
    def call_ai(self, messages: List[Dict]) -> str:
        """Simulated AI call - replace with real OpenAI later"""
        self.show_debug("SENDING TO AI", {"messages": messages, "model": Config.MODEL})
        
        # For now, simulate responses so you can see the flow
        user_message = messages[-1]["content"].lower()
        
        if "weather" in user_message:
            response = "I'll check the weather for you. [TOOL: get_weather]"
        elif "calculate" in user_message or "math" in user_message:
            response = "I'll calculate that. [TOOL: calculator]"
        elif "hello" in user_message:
            response = "Hello! How can I help you today?"
        else:
            response = "I understand you want help with: " + user_message
            
        self.show_debug("AI RESPONDED", response)
        return response
    
    def detect_loop(self, action: str) -> bool:
        """Check if we're about to loop"""
        if action not in self.attempt_counter:
            self.attempt_counter[action] = 0
        
        self.attempt_counter[action] += 1
        
        if self.attempt_counter[action] > Config.MAX_ATTEMPTS:
            self.show_debug(f"LOOP DETECTED! Tried '{action}' {self.attempt_counter[action]} times")
            return True
        
        self.show_debug(f"Attempt #{self.attempt_counter[action]} for action: {action}")
        return False
    
    def process_message(self, user_input: str) -> str:
        """Main agent logic - visible step by step"""
        self.show_debug("STATE", self.state)
        self.show_debug("USER INPUT", user_input)
        
        # Add to conversation history
        self.conversation_history.append({"role": "user", "content": user_input})
        self.show_debug("HISTORY LENGTH", len(self.conversation_history))
        
        # Check for loops before processing
        if self.detect_loop(user_input[:20]):  # Use first 20 chars as action ID
            return "I notice I'm repeating myself. Let me try a different approach or ask for clarification."
        
        # Build messages for AI (including system prompt)
        messages = [
            {"role": "system", "content": "You are a helpful assistant. If you need to use a tool, indicate it with [TOOL: toolname]"}
        ] + self.conversation_history
        
        # Get AI response
        response = self.call_ai(messages)
        
        # Check if AI wants to use a tool
        if "[TOOL:" in response:
            tool = response.split("[TOOL:")[1].split("]")[0].strip()
            self.show_debug(f"AI WANTS TO USE TOOL", tool)
            
            # Check for tool loops
            if self.detect_loop(f"tool_{tool}"):
                response = f"I've tried using {tool} multiple times without success. Can you provide more details?"
            else:
                # Execute tool (simulated)
                tool_result = self.execute_tool(tool)
                response = f"Tool result: {tool_result}"
        
        # Add assistant response to history
        self.conversation_history.append({"role": "assistant", "content": response})
        
        return response
    
    def execute_tool(self, tool_name: str) -> str:
        """Simulate tool execution"""
        self.show_debug(f"EXECUTING TOOL", tool_name)
        
        if tool_name == "get_weather":
            return "Weather: 72°F and sunny"
        elif tool_name == "calculator":
            return "Result: 42"
        else:
            return f"Unknown tool: {tool_name}"
    
    def reset(self):
        """Start fresh"""
        self.show_debug("RESETTING AGENT")
        self.conversation_history = []
        self.attempt_counter = {}
        self.state = "ready"

# Test the agent
if __name__ == "__main__":
    print("=" * 50)
    print("SIMPLE LEARNING AGENT")
    print("=" * 50)
    print("\nThis agent shows you everything it's doing internally.")
    print("Try these commands:")
    print("  - 'What's the weather?'")
    print("  - 'Calculate something'")
    print("  - 'Hello'")
    print("  - Type the same thing 4 times to see loop prevention")
    print("  - 'reset' to start fresh")
    print("  - 'quit' to exit")
    print("\n" + "=" * 50)
    
    agent = VisibleAgent(debug=True)
    
    while True:
        user_input = input("\n👤 You: ").strip()
        
        if user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'reset':
            agent.reset()
            print("🔄 Agent reset!")
            continue
            
        response = agent.process_message(user_input)
        print(f"\n🤖 Agent: {response}")