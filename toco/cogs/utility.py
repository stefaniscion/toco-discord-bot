from discord.ext import commands


class UtilityCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        "Aswers with 'Pong!'"
        await ctx.send("Pong!")
