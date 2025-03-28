import unittest
from chatbot import get_response


class TestChatbot(unittest.TestCase):
    def test_basic_response(self):
        """Test if the chatbot can provide a basic response."""
        response = get_response("Hello, how are you?")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

    def test_error_handling(self):
        """Test if the chatbot handles errors gracefully."""
        # Test with an empty input
        response = get_response("")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

    def test_complex_query(self):
        """Test if the chatbot can handle more complex queries."""
        response = get_response("What is the capital of France?")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
        # The response should be meaningful and contain relevant information
        self.assertTrue(
            any(word in response.lower() for word in ["paris", "france", "capital"])
        )


if __name__ == "__main__":
    unittest.main()
