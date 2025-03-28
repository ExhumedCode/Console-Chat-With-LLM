from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenRouter configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")

if not OPENROUTER_API_KEY or not OPENROUTER_BASE_URL:
    raise ValueError(
        "Please set OPENROUTER_API_KEY and OPENROUTER_BASE_URL in your .env file"
    )

# Initialize the chat model
chat = ChatOpenAI(
    model="google/gemini-2.0-flash-lite-preview-02-05:free",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base=OPENROUTER_BASE_URL,
    temperature=0.7,
)


def get_response(user_input):
    """Get response from the chatbot for user input."""
    messages = [
        SystemMessage(content="You are a helpful and friendly AI assistant."),
        HumanMessage(content=user_input),
    ]

    try:
        response = chat.invoke(messages)
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    """Main function to run the chatbot."""
    print("Welcome to the AI Chatbot! (Type 'quit' to exit)")
    print("-" * 50)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            print("\nGoodbye!")
            break

        if user_input:
            response = get_response(user_input)
            print("\nAI:", response)
        else:
            print("\nPlease enter a valid message.")


if __name__ == "__main__":
    main()
