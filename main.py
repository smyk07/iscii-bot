from hash_logic import iscii_hash
import discord
import os

from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("iscii") or message.content.startswith("ISCII"):
        args = message.content[6:]
        await message.reply(iscii_hash(args))

    if message.content == "!cabbit":
        await message.channel.send(
            "https://media.discordapp.net/attachments/1224994248550780961/1280549417295941795/1000005626.jpg"
        )


client.run(os.getenv("ISCII_TOKEN"))
