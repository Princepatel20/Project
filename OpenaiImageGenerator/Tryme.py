import os
import openai
from config import key

openai.api_key = key
response = openai.Image.create(
  prompt=
  "Imagine a world where cities float in the sky, held up by giant balloons made of crystal. Show me an aerial view of one of these majestic floating cities, with intricate architecture and lush gardens suspended in mid-air.",
  n=1,
  size="1024x1024")
image_url = response['data'][0]['url']
print(image_url)
