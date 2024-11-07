# Author: Niko Lorantos
# https://platform.openai.com/docs/overview for more information

import os
from openai import OpenAI # make sure to 'pip install openai' if you haven't already
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the OpenAI client
api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)