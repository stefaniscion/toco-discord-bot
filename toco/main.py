import os
from dotenv import load_dotenv
from discord import Intents
from toco.client import TocoClient


def main():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")

    intents = Intents.default()
    intents.message_content = True

    client = TocoClient(intents=intents)
    client.run(token)


if __name__ == "__main__":
    main()
