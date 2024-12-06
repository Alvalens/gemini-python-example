import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])


# list model
models = genai.list_models()
for model in models:
    print(model.name)
# Initialize the Image Generation Model
imagen = genai.ImageGenerationModel("imagen-3.0-generate-001")

# Generate images based on the prompt
result = imagen.generate_images(
    prompt="Fuzzy bunnies in my kitchen",
    number_of_images=4,
    safety_filter_level="block_only_high",  # Optional safety settings
    person_generation="allow_adult",  # Controls generation involving people
    aspect_ratio="3:4",  # Image aspect ratio
    negative_prompt="Outside",  # Avoid generating outside scenes
)

# Display or print the image details
for idx, image in enumerate(result.images, start=1):
    print(f"Image {idx}: {image.url}")

    # Optionally display the image (requires PIL/Pillow installed)
    image._pil_image.show()
