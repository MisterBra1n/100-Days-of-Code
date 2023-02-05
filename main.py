import discord
from discord.ext import commands, tasks
import os


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("The bot is ready!")

@bot.event
async def on_message(message):
    if "!" in message.content:
        message.channel.send("You can't say that!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(discord_token)