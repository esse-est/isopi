import discord

bot = discord.Client()

@bot.event
async def on_message(message):
    
    if message.content == "test":
        await message.channel.send("hi!")