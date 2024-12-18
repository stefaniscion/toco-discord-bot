from discord import Message
from discord.ext import commands


class TocoBot(commands.Bot):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message: Message):
        print(f"Message from {message.author}: {message.content}")
        await self.process_commands(message)
