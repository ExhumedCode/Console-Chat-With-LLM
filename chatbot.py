from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import os

# OpenRouter configuration
OPENROUTER_API_KEY = (
    "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"
)
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

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
