import os
import base64
import google.generativeai as genai
from dotenv import load_dotenv

# Configure the Gemini API with your API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Local image path
image_path = "assets/image/test.jpg"

try:
    # Read the local image file
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    # Prepare the prompt for captioning the image
    prompt = "Caption this image."

    # Convert the image to base64 encoding
    encoded_image = base64.b64encode(image_data).decode("utf-8")

    # Generate a response using the model
    response = model.generate_content(
        [{"mime_type": "image/jpeg", "data": encoded_image}, prompt]
    )

    # Print the generated caption response
    print(response.text)

except FileNotFoundError:
    print(f"Image file not found at: {image_path}")
except Exception as e:
    print(f"An error occurred: {e}")
