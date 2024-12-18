import logging
from discord import Message
from discord.ext import commands


class TocoBot(commands.Bot):
    async def on_ready(self):
        logging.info(f"Logged in as {self.user}")

    async def on_message(self, message: Message):
        logging.debug(f"Message from {message.author}: {message.content}")
        await self.process_commands(message)
