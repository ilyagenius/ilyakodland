import discord
from discord.ext import commands
import bot_logic
from bot_logic import *
import openai


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
openai.api_key = 'enter your token here'



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
    result = str(args)
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=result,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You:"]
)
    await ctx.send(embed=discord.Embed(title=f'{result}', description=response['choices'][0]['text']))

bot.run("Enter your token here")
