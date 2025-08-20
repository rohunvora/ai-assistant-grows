# 🧠 AI MEMORY CHEAT SHEET

## THE #1 RULE: AI HAS ALZHEIMER'S
**Every API call, the AI forgets EVERYTHING. You start from zero.**

---

## 🎯 THE ONLY QUESTION THAT MATTERS
> "What does the AI need to know RIGHT NOW to answer this question?"

---

## 📦 MEMORY IS JUST CHOOSING WHAT TO INCLUDE

```
USER SAYS: "Continue the workout"

WHAT AI NEEDS TO KNOW:
✅ Who is this? → "Bob"
✅ What workout? → "Day 3, Leg day" 
✅ Where are we? → "Just finished squats"
✅ Any issues? → "Bad left knee"
❌ Breakfast? → Not relevant!
❌ Job history? → Not relevant!

YOU SEND ALL THIS + THE NEW MESSAGE
```

---

## 🗂️ THE 4 BUCKETS SYSTEM

### 🏷️ BUCKET 1: IDENTITY FACTS
**Who is this person?**
```
Name: Bob
Age: 30
Injuries: Bad knee
Goals: Lose weight
```
→ Include when relevant
→ Store in: JSON file

### 💬 BUCKET 2: RECENT CHAT
**What were we just talking about?**
```
Last 10 messages
Current conversation flow
Today's context
```
→ Always include
→ Store in: Python list

### 📊 BUCKET 3: HISTORICAL DATA
**What happened before?**
```
Workout logs
Past conversations
Previous results
```
→ Only include if specifically needed
→ Store in: Database/CSV

### 🎯 BUCKET 4: CURRENT TASK
**What are we doing right now?**
```
Active workout
Current question
Today's goal
```
→ Always include
→ Store in: Variables

---

## 🔄 THE MEMORY FLOW

```
1. User sends: "What's next?"
                ↓
2. You gather:
   - Facts: "Bob, bad knee"
   - Recent: [last 10 messages]
   - Relevant data: "Today's workout plan"
                ↓
3. You send to AI:
   [System: "You're a coach for Bob who has bad knee"]
   [Chat history: last 10 messages]
   [User: "What's next?"]
                ↓
4. AI responds with context!
```

---

## 📝 DECISION TREE

```
New message arrives
        ↓
Is this a new conversation?
  YES → Start fresh, load identity facts only
  NO → Continue ↓
        ↓
Do I need historical data?
  YES → Query database for specific info
  NO → Continue ↓
        ↓
What facts are relevant?
  - Always: Name, current task
  - Sometimes: Preferences, restrictions
  - Rarely: Old conversations
        ↓
Build the message:
  1. System prompt (identity + role)
  2. Recent conversation (context)
  3. New user message
        ↓
Send to AI!
```

---

## 🎨 VISUAL MEMORY MODEL

```
┌─────────────────────────────────────┐
│          AI BRAIN (Empty)           │
│     "I know nothing, tell me!"      │
└────────────────▲────────────────────┘
                 │
                 │ You send EVERYTHING
                 │ needed for THIS question
                 │
┌────────────────┴────────────────────┐
│         YOUR MEMORY SYSTEM          │
├─────────────────────────────────────┤
│ 📝 Facts DB: Name, age, injuries    │
│ 💬 Recent: Last 10 messages         │
│ 📊 History: All workouts, logs      │
│ 🎯 Current: Today's task            │
└─────────────────────────────────────┘
         ↓              ↓
    Permanent      Temporary
    Storage        Storage
```

---

## 🚫 COMMON MISTAKES

### ❌ WRONG: "The AI will remember"
✅ **RIGHT:** "I must remind the AI"

### ❌ WRONG: Send everything always
✅ **RIGHT:** Send only what's relevant

### ❌ WRONG: Complex memory system first
✅ **RIGHT:** Start simple, add buckets as needed

---

## 💡 MEMORY METHOD QUICK REFERENCE

| Method | What It Is | When To Use | Skill Level |
|--------|------------|-------------|-------------|
| **Full History** | Send everything | Short chats (<20 msgs) | Beginner |
| **Rolling Window** | Last N messages | Most chats | Beginner |
| **Summary + Recent** | Compress old + keep new | Long projects | Intermediate |
| **Fact Extraction** | Store key facts only | Personal assistants | Intermediate |
| **Database/RAG** | Search old convos | Knowledge base | Advanced |

---

## 🎯 YOUR LEARNING PATH

1. **NOW:** Rolling window (last 10 messages)
2. **NEXT:** Add facts file (JSON)
3. **THEN:** Add data storage (CSV)
4. **LATER:** Smart summaries
5. **ADVANCED:** Vector search

---

## 🔑 THE GOLDEN RULE

**Every API call is a fresh start. The AI only knows what you tell it RIGHT NOW.**

Think of it like calling customer service:
- They don't know who you are
- You must explain your issue
- You must provide context
- Every call starts from zero

That's AI memory in a nutshell!