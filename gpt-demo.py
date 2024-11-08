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

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about Hackathons, specifically HackUMass."
        }
    ]
)

output = completion.choices[0].message.content

print(output)