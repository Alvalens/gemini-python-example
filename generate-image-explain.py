import httpx
import os
import base64
import google.generativeai as genai
from dotenv import load_dotenv

# Configure the Gemini API with your API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Image URL to be used for captioning
image_path = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Palace_of_Westminster_from_the_dome_on_Methodist_Central_Hall.jpg/2560px-Palace_of_Westminster_from_the_dome_on_Methodist_Central_Hall.jpg"

try:
    # Download the image using httpx with SSL verification disabled
    with httpx.Client(verify=False) as client:
        image = client.get(image_path)
        image.raise_for_status()  # Raise an exception for bad status codes

    # Prepare the prompt for captioning the image
    prompt = "Caption this image."

    # Convert the image to base64 encoding
    encoded_image = base64.b64encode(image.content).decode("utf-8")

    # Generate a response using the model
    response = model.generate_content(
        [{"mime_type": "image/jpeg", "data": encoded_image}, prompt]
    )

    # Print the generated caption response
    print(response.text)

except httpx.RequestError as e:
    print(f"An error occurred while requesting the image: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
