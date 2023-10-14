import discord
from discord.ext import commands
import bot_logic
from bot_logic import *



intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     if message.content.startswith('$hello'):
#         await message.channel.send("Hi!")
#     elif message.content.startswith('$bye'):
#         await message.channel.send("\\U0001f642")
#     else:
#         await message.channel.send(message.content)
#
# @bot.event
# async def on_message(message):
#     if message.content.startswith('Genpass'):
#         await message.channel.send(gen_pass(10))
#
# @bot.event
# async def on_message(message):
#     if message.content.startswith('Createemoji'):
#         await message.channel.send(gen_emodji())

# @bot.event
# async def on_message(message):
#     if message.content.startswith('Flipcoin'):
#         await message.channel.send(flip_coin())
        
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)



bot.run("")
