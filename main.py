import iscii
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

    if (
        message.content.startswith("iscii")
        or message.content.startswith("Iscii")
    ):
        if len(message.content) > 6:
            args = message.content[6:]
            await message.reply(f"{iscii.encode(args)}\n-# [Know more](<https://github.com/smyk07/iscii-bot>)")
        else:
            await message.add_reaction("😹")

    if (
        message.content.startswith("isciidecode")
        or message.content.startswith("Isciidecode")
    ): 
        if len(message.content) > 12: 
            args = message.content[12:]
            await message.reply(f"{iscii.decode(args)}\n-# [Know more](<https://github.com/smyk07/iscii-bot>)")
        else:
            await message.add_reaction("😹")


    if message.content == "!cabbit":
        await message.channel.send(
            "https://media.discordapp.net/attachments/1224994248550780961/1280549417295941795/1000005626.jpg"
        )


client.run(os.getenv("ISCII_TOKEN"))
