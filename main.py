import json
import random

import discord
from discord.ext import commands
import openai
import requests
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
openai.api_key = ''
Token = ''



@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command(name='gpt')
async def cont(ctx: commands.context, *, args):
    """answers like chatgpt"""
    result = str(args)
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= result,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You:"]
)
    await ctx.send(embed=discord.Embed(title=f'{result}', description=response['choices'][0]['text']))


@bot.command(name='getweather')
async def getweather(ctx, *, city: str):
    """The weather in Moscow"""
    city_name = city
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Token}&units=metric')
    data = json.loads(res.text)
    await ctx.send(f'Погода в {city_name} - {data["main"]["temp"]}')


@bot.command(name='recycle')
async def cont(ctx: commands.context, *, args):
    """answers like chatgpt"""
    result = str(args)
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= f'Перерабатывается{result}',
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You:"]
)
    await ctx.send(embed=discord.Embed(title=f'{result}', description=response['choices'][0]['text']))

bot.run("")
