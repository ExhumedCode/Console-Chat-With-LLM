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
   pip install langchain openai
   ```

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
