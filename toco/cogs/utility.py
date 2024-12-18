from discord.ext import commands


class UtilityCommands(commands.Cog):
    """Cog containing utility commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Answers with 'Pong!'"""
        await ctx.send("Pong!")
