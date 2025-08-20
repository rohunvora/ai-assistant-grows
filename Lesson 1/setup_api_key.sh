#!/bin/bash
# Quick setup script for API key

echo "Setting up OpenAI API key..."
echo ""
echo "Choose a method:"
echo "1. Create .env file (easiest for development)"
echo "2. Set environment variable (best for production)"
echo "3. Just tell me what to do"
echo ""
read -p "Choice (1-3): " choice

case $choice in
    1)
        read -p "Enter your OpenAI API key: " api_key
        echo "OPENAI_API_KEY=$api_key" > .env
        echo "✅ Created .env file"
        echo "   Your API key will be loaded automatically"
        ;;
    2)
        read -p "Enter your OpenAI API key: " api_key
        echo ""
        echo "Add this line to your ~/.zshrc or ~/.bash_profile:"
        echo "export OPENAI_API_KEY=$api_key"
        echo ""
        echo "Then run: source ~/.zshrc"
        ;;
    3)
        echo ""
        echo "OPTION 1 - Easiest (just for this project):"
        echo "  Create a file called .env with one line:"
        echo "  OPENAI_API_KEY=sk-your-key-here"
        echo ""
        echo "OPTION 2 - System-wide:"
        echo "  Add to ~/.zshrc:"
        echo "  export OPENAI_API_KEY=sk-your-key-here"
        echo ""
        echo "OPTION 3 - Temporary (this terminal only):"
        echo "  Run: export OPENAI_API_KEY=sk-your-key-here"
        ;;
esac