import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("Bot is now ready to use")
    print("------------------------")

# welcome
@client.event
async def on_member_join(member):
    channel = client.get_channel(1264154912065982518)
    await channel.send("Hello")

# leave (FIXED event name)
@client.event
async def on_member_remove(member):
    channel = client.get_channel(1264154912065982518)
    await channel.send("Goodbye")

@client.command()
async def hello(ctx):
    await ctx.send("How can I help you today?")

@client.command()
async def call(ctx):
    await ctx.send("Ring ring 🔔")


@client.command()
async def roll(ctx):
    randomNumber = input()
    await ctx.send(f"Dice rolled!🎲 {randomNumber}")



























client.run("")