# Memory Methods for AI Agents - Complete Guide

## Method 1: Full History (What We Just Built)

### How It Works
```python
conversation = [
    {"role": "user", "content": "Message 1"},
    {"role": "assistant", "content": "Response 1"},
    {"role": "user", "content": "Message 2"},
    {"role": "assistant", "content": "Response 2"},
    # ... keeps growing forever
]
# Send EVERYTHING every time
```

### Best For:
- Short conversations (< 20 messages)
- Customer support chats
- Quick tasks
- When you need perfect recall

### Problems:
- Gets expensive fast (each message costs more)
- Hits token limits (~8,000 tokens for gpt-4o-mini)
- Slows down over time

### Real Example:
```
Message 1: 25 tokens ($0.000004)
Message 10: 500 tokens ($0.00008)
Message 50: 5,000 tokens ($0.0008) ← Getting pricey!
Message 100: FAILS - too many tokens!
```

## Method 2: Rolling Window (Keep Last N Messages)

### How It Works
```python
MAX_MESSAGES = 10  # Only keep last 10

if len(conversation) > MAX_MESSAGES:
    conversation = conversation[-MAX_MESSAGES:]  # Drop old ones
```

### Best For:
- Long conversations
- Chat apps
- When recent context matters most
- Budget-conscious apps

### Problems:
- Forgets older information
- Can lose important context

### Real Example:
```
User: "My name is Bob"
[... 20 messages later ...]
User: "What's my name?"
AI: "I don't know" ← Forgot because we dropped that message!
```

## Method 3: Summary + Recent (Smart Hybrid)

### How It Works
```python
# Keep a summary of old conversation
summary = "User (Bob) discussed project requirements..."

# Plus recent messages
recent_messages = [last 5 messages]

# Send both
messages = [
    {"role": "system", "content": f"Previous context: {summary}"},
    *recent_messages
]
```

### Best For:
- Long technical discussions
- Project planning
- Medical/legal consultations
- When you need both history AND details

### Real Example:
```
Summary: "User Bob is building a website, wants blue theme, needs login"
Recent: [last 5 messages about specific button placement]
```

## Method 4: Fact Extraction (Database Memory)

### How It Works
```python
facts = {
    "user_name": "Bob",
    "preferences": {"color": "blue", "theme": "dark"},
    "current_task": "building website"
}

# Include facts in system prompt
system_prompt = f"User info: {json.dumps(facts)}"
```

### Best For:
- Personal assistants
- CRM systems
- Long-term relationships
- When specific facts matter more than conversation flow

### Real Example:
```
Extracted facts:
- Name: Bob
- Location: NYC
- Prefers Python
- Working on: AI agent

These facts persist across sessions!
```

## Method 5: RAG (Retrieval Augmented Generation)

### How It Works
```python
# Store all messages in a database
database.store(message, embedding)

# When user asks something, search for relevant past messages
relevant_history = database.search(current_question, limit=5)

# Only send relevant pieces
messages = [current_question] + relevant_history
```

### Best For:
- Knowledge bases
- Documentation bots
- Huge conversation histories
- When you need to find specific past discussions

### Problems:
- Complex to implement
- Needs vector database
- Can miss context

## Custom Instructions (System Prompts)

### What They Are
The "system" message that goes FIRST in every conversation:

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant. Remember the user's name and preferences."},
    {"role": "user", "content": "Hi, I'm Bob"},
    # ... rest of conversation
]
```

### Common Patterns:

**For Memory-Aware Agents:**
```python
system_prompt = """
You are a helpful assistant with conversation memory.
Key facts about the user:
{extracted_facts}

Previous conversation summary:
{summary}

Remember to:
- Reference previous discussions when relevant
- Maintain consistency with established facts
- Ask for clarification if something contradicts earlier info
"""
```

**For Customer Service:**
```python
system_prompt = """
You are a customer service agent.
Always:
- Reference previous issues mentioned
- Remember customer preferences
- Note any unresolved problems
"""
```

**For Technical Assistants:**
```python
system_prompt = """
You are a coding assistant.
Track:
- Current project details
- Technology stack being used  
- Problems already solved
- User's skill level
"""
```

## When to Use Each Method

### Quick Decision Tree:

```
Is conversation < 20 messages?
  → Use Full History

Is conversation long but only recent matters?
  → Use Rolling Window

Need both long-term memory and recent detail?
  → Use Summary + Recent

Building a personal assistant?
  → Use Fact Extraction

Have thousands of conversations to search?
  → Use RAG

Just starting out learning?
  → Use Full History (simplest!)
```

## Common Implementation Mistakes

### Mistake 1: Not Including System Messages
```python
# WRONG - loses AI responses
conversation = [user_messages_only]

# RIGHT - include both sides
conversation = [
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."},
]
```

### Mistake 2: Forgetting Token Limits
```python
# WRONG - will eventually crash
conversation.append(new_message)  # Forever

# RIGHT - check limits
if count_tokens(conversation) > 7000:
    conversation = summarize_or_trim(conversation)
```

### Mistake 3: Not Persisting Memory
```python
# WRONG - memory dies when program stops
conversation = []

# RIGHT - save to file/database
with open("conversation.json", "w") as f:
    json.dump(conversation, f)
```

## For Your Learning Journey

**Start with:** Full History (what we built)
**Then add:** Token counting and limits
**Then try:** Rolling window
**Finally:** Summary + Recent for real apps

The key insight: The AI has NO built-in memory. Whatever memory exists, YOU are managing it by deciding what to send with each request.