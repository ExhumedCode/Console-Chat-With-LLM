# AI Chatbot

A simple console-based chatbot that uses OpenRouter API with the Gemini model to answer questions.

## Setup Instructions

1. Create and activate a Python virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Unix/macOS
   # or
   .\venv\Scripts\activate  # On Windows
   ```

2. Install required packages:

   ```bash
   pip install langchain openai python-dotenv
   ```

3. Set up environment variables:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your OpenRouter API key:
     ```
     OPENROUTER_API_KEY=your_openrouter_api_key_here
     OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
     ```
   - Get your API key from [OpenRouter](https://openrouter.ai/keys)

## Running the Application

1. Make sure your virtual environment is activated
2. Run the chatbot:
   ```bash
   python chatbot.py
   ```
3. Type your questions and press Enter
4. Type 'quit' to exit the application

## Running Tests

To run the test suite:

```bash
python -m unittest test_chatbot.py
```

## Features

- Interactive console interface
- Powered by Google's Gemini model through OpenRouter API
- Simple and intuitive usage
- Error handling for failed requests
- Test suite for basic functionality verification
- Secure API key management using environment variables

## Security Note

This project uses environment variables to securely manage API keys. Never commit your `.env` file or expose your API keys in the code. The `.env` file is already included in `.gitignore` to prevent accidental commits.
