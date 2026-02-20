API = "AIzaSyAGgh02-Nrl-3yCaP6nkcXrjiJmHO8eJwg"

import asyncio
from google import genai


async def generate(prompt):

    client = genai.Client(api_key=API)

    response = await client.aio.models.generate_content(
        model="gemma-3-27b-it",
        contents=prompt,
    )
    
    return response.text

if __name__ == "__main__":
    print(asyncio.run(generate(input())))