import os
import asyncio
from dotenv import load_dotenv
from discord import Intents
from toco.bot import TocoBot
from toco.cogs.utility import UtilityCommands


async def load_bot():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    intents = Intents.default()
    intents.message_content = True

    bot = TocoBot(command_prefix="/", intents=intents)

    await bot.add_cog(UtilityCommands(bot))
    await bot.start(token)


def main():
    asyncio.run(load_bot())


if __name__ == "__main__":
    asyncio.run(load_bot())
