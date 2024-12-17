from discord import Intents
from toco.client import TocoClient


def main():
    intents = Intents.default()
    intents.message_content = True

    client = TocoClient(intents=intents)
    client.run("")


if __name__ == "__main__":
    main()
