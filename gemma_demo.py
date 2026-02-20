from browser_use.llm import ChatGoogle
from browser_use import Agent
from dotenv import load_dotenv
import asyncio

load_dotenv()

agent = Agent(
    task="Compare the price of gpt-4o and DeepSeek-V3",
    llm=ChatGoogle(
        model="gemma-3-27b-it",
        include_system_in_user=True,
        supports_structured_output=False,
    ),
    max_actions_per_step=1
)

result = asyncio.run(agent.run())
print(result)