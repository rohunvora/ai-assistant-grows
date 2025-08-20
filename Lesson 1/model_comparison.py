#!/usr/bin/env python3
"""
MODEL COMPARISON TOOL
See how different models respond to the same question
And compare their costs!
"""

import requests
import time

# Read API key
with open('.env', 'r') as f:
    line = f.read().strip()
    api_key = line.split('OPENAI_API_KEY=')[1].strip()

# Available models and their costs (per 1M tokens)
MODELS = {
    "gpt-3.5-turbo": {
        "name": "GPT-3.5 Turbo",
        "cost_per_million": 0.50,
        "description": "Older, cheaper, still decent"
    },
    "gpt-4o-mini": {
        "name": "GPT-4o Mini", 
        "cost_per_million": 0.15,
        "description": "Best value! Fast & cheap"
    },
    "gpt-4o": {
        "name": "GPT-4o",
        "cost_per_million": 5.00,
        "description": "Most capable, expensive"
    }
}

def call_model(model_id, message):
    """Call a specific model with a message"""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model_id,
        "messages": [{"role": "user", "content": message}],
        "temperature": 0.7,
        "max_tokens": 150  # Limit response length to save money
    }
    
    start_time = time.time()
    
    try:
        response = requests.post(url, headers=headers, json=data)
        elapsed = time.time() - start_time
        
        if response.status_code == 200:
            result = response.json()
            return {
                "success": True,
                "response": result["choices"][0]["message"]["content"],
                "tokens": result["usage"]["total_tokens"],
                "time": elapsed,
                "model_used": result["model"]  # Actual model version
            }
        else:
            return {
                "success": False,
                "error": f"Error {response.status_code}: {response.text}"
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def compare_models(question):
    """Compare all models with the same question"""
    print("\n" + "=" * 60)
    print(f"QUESTION: {question}")
    print("=" * 60)
    
    results = []
    
    for model_id, info in MODELS.items():
        print(f"\n🤖 Testing {info['name']} ({model_id})...")
        print(f"   {info['description']}")
        
        result = call_model(model_id, question)
        
        if result["success"]:
            tokens = result["tokens"]
            cost = (tokens / 1_000_000) * info["cost_per_million"]
            
            print(f"\n   📝 RESPONSE FROM {info['name'].upper()}:")
            print(f"   {'-' * 40}")
            print(f"   {result['response'][:300]}...")
            if len(result['response']) > 300:
                print("   [truncated for display]")
            print(f"   {'-' * 40}")
            print(f"\n   📊 Stats:")
            print(f"      Time: {result['time']:.2f} seconds")
            print(f"      Tokens: {tokens}")
            print(f"      Cost: ${cost:.8f}")
            print(f"      Actual model: {result['model_used']}")
            
            results.append({
                "model": info['name'],
                "tokens": tokens,
                "cost": cost,
                "time": result['time']
            })
        else:
            print(f"   ❌ Failed: {result['error']}")
    
    # Show comparison
    if results:
        print("\n" + "=" * 60)
        print("COMPARISON SUMMARY")
        print("=" * 60)
        
        # Find cheapest
        cheapest = min(results, key=lambda x: x['cost'])
        fastest = min(results, key=lambda x: x['time'])
        
        print("\n📊 Results:")
        for r in results:
            print(f"\n   {r['model']}:")
            print(f"      Cost: ${r['cost']:.8f}", end="")
            if r == cheapest:
                print(" 🏆 CHEAPEST", end="")
            print()
            print(f"      Time: {r['time']:.2f}s", end="")
            if r == fastest:
                print(" 🏆 FASTEST", end="")
            print()
            print(f"      Tokens: {r['tokens']}")
        
        # Cost comparison
        if len(results) > 1:
            mini_cost = next((r['cost'] for r in results if 'Mini' in r['model']), 0)
            gpt4_cost = next((r['cost'] for r in results if 'GPT-4o' in r['model'] and 'Mini' not in r['model']), 0)
            
            if mini_cost > 0 and gpt4_cost > 0:
                ratio = gpt4_cost / mini_cost
                print(f"\n💡 GPT-4o is {ratio:.1f}x more expensive than GPT-4o-mini for this question")

def main():
    print("=" * 60)
    print("AI MODEL COMPARISON TOOL")
    print("=" * 60)
    print("\nThis tool sends the same question to different models")
    print("so you can see the difference in quality, speed, and cost.")
    
    print("\n📋 Available models:")
    for model_id, info in MODELS.items():
        cost = info['cost_per_million']
        print(f"   • {info['name']}: ${cost:.2f} per million tokens")
    
    print("\n" + "-" * 60)
    print("\nTry these example questions:")
    print("1. 'What is 2+2?'")
    print("2. 'Write a haiku about programming'")
    print("3. 'Explain quantum computing in simple terms'")
    print("4. 'What's the bug in this code: for i in range(10) print(i)'")
    print("\nOr type your own question!")
    print("Type 'quit' to exit")
    print("-" * 60)
    
    while True:
        print()
        question = input("Your question: ").strip()
        
        if question.lower() == 'quit':
            break
        
        if question.isdigit() and 1 <= int(question) <= 4:
            # Use example question
            examples = [
                "What is 2+2?",
                "Write a haiku about programming",
                "Explain quantum computing in simple terms",
                "What's the bug in this code: for i in range(10) print(i)"
            ]
            question = examples[int(question) - 1]
            print(f"Using example: {question}")
        
        compare_models(question)
        
        print("\n" + "-" * 60)
        print("Try another question or type 'quit' to exit")

if __name__ == "__main__":
    main()