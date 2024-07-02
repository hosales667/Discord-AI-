import discord
from discord.ext import commands
from config import TOKEN
from io import BytesIO
import requests 
from PIL import Image
from clasification import classificate_image

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def classificate(ctx: commands.Context):
    if ctx.message.attachments:
        response = requests.get(ctx.message.attachments[0])
        image = Image.open(BytesIO(response.content))
        result = classificate_image(image)
        text = {'Lion': 'лев', 'Rat': 'крыса', 'Cat': 'кошка'}[result[0]] 
        await ctx.send(
            f"На картинке {text} с вероятностью {round(result[1]*100)}%"
        )
    else:
        await ctx.send('Ошибка: вы не добавили картинку')

bot.run(TOKEN)
