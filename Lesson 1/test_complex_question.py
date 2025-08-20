#!/usr/bin/env python3
"""
Test a complex question on different models
To see if expensive models are actually better
"""

import requests

# Read API key
with open('.env', 'r') as f:
    line = f.read().strip()
    api_key = line.split('OPENAI_API_KEY=')[1].strip()

# Complex question that might show quality differences
complex_question = """
Find the bug in this Python code and explain why it happens:

def remove_duplicates(lst):
    for i in range(len(lst)):
        if lst[i] in lst[i+1:]:
            lst.remove(lst[i])
    return lst

numbers = [1, 2, 2, 3, 3, 3, 4]
print(remove_duplicates(numbers))
"""

def test_model(model_id, model_name):
    """Test a model with the complex question"""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model_id,
        "messages": [{"role": "user", "content": complex_question}],
        "temperature": 0.3,  # Lower temperature for more consistent technical answers
        "max_tokens": 300
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        answer = result["choices"][0]["message"]["content"]
        tokens = result["usage"]["total_tokens"]
        
        print(f"\n{'='*60}")
        print(f"🤖 {model_name} ({model_id})")
        print(f"{'='*60}")
        print(answer)
        print(f"\n📊 Tokens used: {tokens}")
        
        # Calculate cost
        costs = {"gpt-3.5-turbo": 0.50, "gpt-4o-mini": 0.15, "gpt-4o": 5.00}
        cost_per_million = costs.get(model_id, 0.15)
        cost = (tokens / 1_000_000) * cost_per_million
        print(f"💰 Cost: ${cost:.8f}")

print("COMPLEX QUESTION TEST: Finding a tricky bug")
print("=" * 60)
print("\nQuestion: Finding and explaining a bug in Python code")
print("\nLet's see if more expensive models give better answers...")

# Test each model
test_model("gpt-4o-mini", "GPT-4o Mini (Cheap)")
test_model("gpt-4o", "GPT-4o (Expensive)")

print("\n" + "=" * 60)
print("WHICH ANSWER WAS BETTER?")
print("Did the expensive model provide more value?")
print("For coding questions, sometimes yes!")
print("For simple questions, usually no!")
print("=" * 60)