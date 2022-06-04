import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv(DISCORD_TOKEN)

bot = commands.Bot("!")


@bot.command()
async def play():
    pass

bot.run(TOKEN)
