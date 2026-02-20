from browser_use import Agent, ChatGoogle
import asyncio
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogle(model="gemini-2.5-flash-lite")
llm = ChatGoogle(model="gemini-2.5-flash-lite-preview-09-2025")
llm = ChatGoogle(model="gemma-3-27b-it")

# Create and run the agent
async def main(prompt):
    agent = Agent(
        task=prompt,
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main("play the daily wordle at https://www.nytimes.com/games/wordle/index.html"))