from discord.ext import commands


class MusicCommands(commands.Cog):
    """Cog containing commands about music"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx: commands.Context):
        """Joins the voice channel of the user"""
        if ctx.author.voice is None:
            await ctx.send("Non sei in un canale vocale")
            return

        channel = ctx.author.voice.channel

        try:
            if ctx.voice_client is None:
                await channel.connect()
                await ctx.send(f"Mi sono unito al canale vocale: **{channel.name}**!")

            else:
                await ctx.voice_client.move_to(channel)
                await ctx.send(
                    f"Mi sono spostato nel canale vocale: **{channel.name}**!"
                )
        except Exception as e:
            await ctx.send(f"Errore: {e}")
