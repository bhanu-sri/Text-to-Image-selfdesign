import requests
from PIL import Image
from io import BytesIO

def generate_image_from_text(text_description):
    # Replace with your Hugging Face Space API URL
    api_url = "https://api-inference.huggingface.co/models/bhanusrikowru/stable-diffusion-outfit-generator"
    headers = {"Authorization": "Bearer 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"}

    response = requests.post(api_url, headers=headers, json={"inputs": text_description})

    if response.status_code == 200:
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        return image
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")
