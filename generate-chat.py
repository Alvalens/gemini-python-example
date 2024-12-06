import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You're a mental health professional. Provide support to a patient who is feeling anxious.",
)

try:
    # Start a chat session
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": ["Hello"]},
            {
                "role": "model",
                "parts": ["Great to meet you. How can I help you today?"],
            },
        ]
    )

    print("Chat session started. Type 'quit' or 'exit' to end the conversation.")

    while True:
        # Get user input
        user_input = input("You: ").strip()

        # Check for exit command
        if user_input.lower() in ["quit", "exit"]:
            print("Ending chat session...")
            break

        # Validate input
        if not user_input:
            print("Please enter a valid message.")
            continue

        try:
            # Send user input to the model and get response
            response = chat.send_message(user_input)

            # Print the model's response
            print(f"Model: {response.text}")

        except Exception as e:
            print(f"Error during chat: {str(e)}")
            print("Please try again or type 'exit' to quit.")

except Exception as e:
    print(f"Error initializing chat: {str(e)}")
