import httpx
import os
import base64
import google.generativeai as genai

# Configure the Gemini API with your API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Initialize the model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Image URL to be used for captioning
image_path = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Palace_of_Westminster_from_the_dome_on_Methodist_Central_Hall.jpg/2560px-Palace_of_Westminster_from_the_dome_on_Methodist_Central_Hall.jpg"

# Download the image using httpx
image = httpx.get(image_path)

# Prepare the prompt for captioning the image
prompt = "Caption this image."

# Convert the image to base64 encoding
encoded_image = base64.b64encode(image.content).decode("utf-8")

# Generate a response using the model by passing both the image and the prompt
response = model.generate_content(
    [{"mime_type": "image/jpeg", "data": encoded_image}, prompt]
)

# Print the generated caption response
print(response.text)
