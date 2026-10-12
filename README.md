# My First LLM Bot 🤖

A terminal chatbot built with the Anthropic Claude API that remembers the conversation.

## What it does
- Chat with Claude directly from the terminal
- Keeps the full conversation history, so the bot remembers context (e.g. your name)
- Handles the model's response blocks, separating the reasoning ("thinking") from the final answer ("text")
- Type `sair` to exit

## How to run
1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install anthropic python-dotenv
   ```
2. Create a `.env` file with your API key:
   ```
   ANTHROPIC_API_KEY=your_key_here
   ```
3. Run:
   ```bash
   python chat.py
   ```

## What I learned
- **LLMs are stateless:** the model doesn't remember anything. Memory comes from sending the whole message history (`user` / `assistant` roles) on every call.
- **Response structure:** the API returns a list of content blocks; I filter by `type` to get the answer.
- **Secrets management:** API keys live in `.env` and are excluded via `.gitignore`.

## Next steps
- [ ] Add a system prompt with a custom personality
- [ ] Stream responses token by token
- [ ] Build a simple web UI
