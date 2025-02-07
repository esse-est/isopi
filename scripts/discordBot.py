import nextcord
from nextcord.ext import commands


def start(key: str):
    bot = commands.Bot()

    @bot.slash_command(description="Replies with pong!")
    async def ping(interaction: nextcord.Interaction):
        await interaction.send("Pong!", ephemeral=True)

    bot.run(key)