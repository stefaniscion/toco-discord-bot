import os
import asyncio
from dotenv import load_dotenv
from discord import Intents
from discord.ext import commands
from toco.bot import TocoBot
from toco.cogs.utility import UtilityCommands

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
intents = Intents.default()
intents.message_content = True


async def setup_cogs(bot: commands.Bot):
    """Adds the cogs to the bot"""
    await bot.add_cog(UtilityCommands(bot))


async def start_bot():
    """Starts the bot"""
    bot = TocoBot(command_prefix="/", intents=intents)
    await setup_cogs(bot)
    await bot.start(token)


def main():
    asyncio.run(start_bot())


if __name__ == "__main__":
    asyncio.run(start_bot())
