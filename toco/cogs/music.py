import asyncio
import logging
from discord import FFmpegOpusAudio
from discord.ext import commands
from discord.voice_client import VoiceClient
import yt_dlp


class MusicCommands(commands.Cog):
    """Cog containing commands about music"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.queues = {}
        self.voice_clients: dict[VoiceClient] = {}
        self.YTDL_OPTIONS = {
            "format": "bestaudio/best",
        }
        self.yt_dl = yt_dlp.YoutubeDL(self.YTDL_OPTIONS)
        self.FFMPEG_OPTIONS = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": '-vn -filter:a "volume=0.25"',
        }

    @commands.command()
    async def play(self, ctx: commands.Context, *, track_request: str):
        """Play a song, or add it to the queue"""
        try:
            voice_client = await self._join(ctx)
            track = await self._parse_track_request(track_request)
            player = FFmpegOpusAudio(track["stream_url"], **self.FFMPEG_OPTIONS)
            voice_client.play(player)
            await ctx.send(f"Riproduco: **{track['title']}**\n{track['webpage_url']}\n")
        except Exception as e:
            logging.error(f"Error while playing track: {e}")

    async def _join(self, ctx: commands.Context) -> VoiceClient:
        """Joins the voice channel of the user"""
        if ctx.author.voice is None:
            await ctx.send("Non sei in un canale vocale")
            return

        channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            voice_client = await channel.connect()
            await ctx.send(f"Mi sono unito al canale vocale: **{channel.name}**!")

        else:
            voice_client = await ctx.voice_client.move_to(channel)
            await ctx.send(f"Mi sono spostato nel canale vocale: **{channel.name}**!")

        self.voice_clients[ctx.guild.id] = voice_client
        return voice_client

    async def _parse_track_request(self, track_request: str) -> dict:
        """Parses a song, that can be a URL, a search query, or a file"""
        if "youtube.com" in track_request or "youtu.be" in track_request:
            track = await self._parse_youtube_url(track_request)
        return track

    async def _parse_youtube_url(self, track_request: str) -> dict:
        """Parses a YouTube URL"""
        loop = asyncio.get_event_loop()
        info = await loop.run_in_executor(
            None, lambda: self.yt_dl.extract_info(track_request, download=False)
        )
        track = {
            "title": info["title"],
            "webpage_url": info["webpage_url"],
            "stream_url": info["url"],
        }
        return track
