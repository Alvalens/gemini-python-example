import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_local_video(video_path):
    try:
        # Print upload status
        print(f"Uploading video file: {video_path}")
        video_file = genai.upload_file(path=video_path)
        print(f"Upload completed: {video_file.uri}")

        # Check processing status
        while video_file.state.name == "PROCESSING":
            print(".", end="")
            time.sleep(10)
            video_file = genai.get_file(video_file.name)

        if video_file.state.name == "FAILED":
            raise ValueError(f"Video processing failed: {video_file.state.name}")

        # Initialize model
        model = genai.GenerativeModel("gemini-1.5-pro")

        # Create prompt
        prompt = """
        Please describe the content of the video.
        """

        # Generate response
        print("\nAnalyzing video content...")
        response = model.generate_content(
            [video_file, prompt], request_options={"timeout": 600}
        )

        return response.text

    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    video_path = "assets/videos/test.mp4"
    result = analyze_local_video(video_path)
    print("\nVideo Analysis:")
    print(result)
