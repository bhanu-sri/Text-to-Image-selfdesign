from flask import Flask, render_template, request, send_from_directory
from diffusers import StableDiffusionPipeline
import torch
import os

app = Flask(__name__)

# Load the model
model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
model = model.to("cuda" if torch.cuda.is_available() else "cpu")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    description = request.form['description']
    image = model(description).images[0]
    image_path = os.path.join('static', 'outputs', 'output.png')
    image.save(image_path)
    return send_from_directory('static/outputs', 'output.png')

if __name__ == '__main__':
    app.run(debug=True)
