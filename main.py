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

    if message.content.startswith("isciie") or message.content.startswith("Isciie"):
        if len(message.content) > 7:
            args = message.content[7:]
            await message.reply(iscii.encode(args))
        elif message.reference:
            replied_message = await message.channel.fetch_message(
                message.reference.message_id
            )
            await replied_message.reply(iscii.encode(replied_message.content))
        else:
            await message.add_reaction("😹")

    if message.content.startswith("isciid") or message.content.startswith("Isciid"):
        if len(message.content) > 7:
            args = message.content[7:]
            await message.reply(iscii.decode(args))
        elif message.reference:
            replied_message = await message.channel.fetch_message(
                message.reference.message_id
            )
            await replied_message.reply(iscii.decode(replied_message.content))
        else:
            await message.add_reaction("😹")

    if message.content == "!cabbit":
        await message.channel.send(
            "https://media.discordapp.net/attachments/1224994248550780961/1280549417295941795/1000005626.jpg"
        )


client.run(os.getenv("ISCII_TOKEN"))
