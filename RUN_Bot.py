import discord
import asyncio
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from discord.ext.commands import Bot

imageFile = Image.open("src.png")
font = ImageFont.truetype('arial.ttf', 90) 

bot = commands.Bot(command_prefix='Useless')

@bot.event
async def on_ready():
    print("Bot: "+str(bot.user)+" Ready!")

@bot.event
async def on_message(message):
    if message.author != bot.user:

        imageEdit = ImageDraw.Draw(imageFile)       
        imageEdit.text((30,120), message.author.name, (255, 255, 255), font=font)       
        imageFile.save("result.png")
        
        image = [
            discord.File('result.png')
        ]
      
        channel = message.channel       
        await channel.send("",files=image)
        print("Silenced "+message.author.name)

bot.run('NzA3OTYxMzQ4NTQ5NjQwMjQz.XrQaYg.2tlSDgZJLU_iTf-V_GkA4y7E8Tg')







