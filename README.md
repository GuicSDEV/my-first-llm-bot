# My First LLM Bot

A command-line chatbot built with Python and the Anthropic API. It sends the conversation history with each request and can save that history as a JSON file.

## Requirements

- Python 3.10 or newer
- An Anthropic API key

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install the dependencies:

   ```bash
   pip install anthropic python-dotenv pytest
   ```

3. Create a `.env` file in the project directory and add your API key:

   ```dotenv
   ANTHROPIC_API_KEY=your_api_key
   ```

   `.env` and `.venv/` are excluded from Git by `.gitignore`.

## Run

```bash
python chat.py
```

Enter a message to chat. The available commands are:

- `sair` exits the program.
- `/reset` clears the conversation currently held in memory.
- `/save` prompts for a JSON file path and saves the conversation. Press Enter at the path prompt to use `saved_chat.json`.

The bot uses the system prompt `Você é um tutor, paciente que responde em português` and defaults to the `claude-haiku-5-5` model. The model and system prompt can be changed when constructing `ChatBot` in `chat.py`.

Saved JSON files are not loaded automatically when the program starts. The conversation is kept in memory while the program runs, unless you explicitly save it.

## Tests

Run the test suite with:

```bash
pytest
```

The current tests cover initial history, resetting the conversation, and saving it to a file.

## What I Learned

- **The model does not retain local conversation state.** The app stores user and assistant messages in `save_chat` and sends that history with each API request to provide conversational context.
- **API responses contain content blocks.** This bot adds the text from blocks whose type is `text` to the reply; it does not separately handle or display other block types.
- **A system prompt sets the assistant's instructions.** It is passed separately from the user/assistant message history on every request.
- **Saving and loading are separate features.** The bot can write the in-memory history to JSON, but currently does not restore a saved conversation on startup.
- **Keep credentials out of source control.** `python-dotenv` loads the API key from `.env`, and `.gitignore` excludes that file from Git.
