# AI Agent Learning Notes

## How AI APIs Actually Work

### The Simple Truth
When you use an AI API, you're just sending text and getting text back. That's it.

```
YOU SEND:
{
  "messages": [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "What's 2+2?"}
  ],
  "model": "gpt-4o-mini"
}

API RETURNS:
{
  "choices": [{
    "message": {
      "content": "2+2 equals 4"
    }
  }]
}
```

### Key Concepts Demystified

**System Prompt**: Just instructions at the start. Like telling someone "You're a math tutor" before asking questions.

**Model Selection**: 
- `gpt-4o-mini`: Fast, cheap, good for most tasks ($0.15 per 1M tokens)
- `gpt-4o`: Smarter, more expensive ($5 per 1M tokens)
- Think of it like choosing between a Honda Civic vs BMW - both drive, different costs

**API Keys**: Just a password that proves you can use the service. Like a Netflix login.

**Environment Variables (.env)**: 
- Just a text file that stores secrets
- Keeps passwords out of your code
- Never share or commit to GitHub

## Common Confusion Points

### "How does the AI remember things?"
**It doesn't!** You must send the entire conversation history every time:

```
First call: [user: "I'm Bob"]
AI responds: "Hi Bob!"

Second call: [user: "I'm Bob", assistant: "Hi Bob!", user: "What's my name?"]
AI responds: "Your name is Bob"

If you only sent: [user: "What's my name?"]
AI responds: "I don't know your name"
```

### "Why do agents get stuck in loops?"
Because they forget what they already tried:

```
BAD AGENT:
Try A → Fails
Forgets it tried A
Try A → Fails
Forgets it tried A
[Infinite loop]

GOOD AGENT:
Try A → Fails → Record "A failed"
Check records → "A already failed"
Try B instead
```

## What We'll Build To Learn

### Phase 1: See The Flow
Build an agent that shows you EVERYTHING:
- What it sends to the API
- What it gets back
- How it decides what to do next
- When it's about to loop

### Phase 2: Control The Brain
Add controls to prevent common failures:
- Max attempts counter (visible)
- State memory (what's been tried)
- Fallback options (when stuck)

### Phase 3: Give It Tools
Let the agent do things:
- But show WHY it chose each tool
- Display the decision process
- Make failures visible and understandable