import discord, requests, os
from commands.status.embeds.createStatusEmbed import createStatusEmbed
from commands.status.statusButtons import *
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")

async def showStatus(interaction: discord.Interaction):
    embed = await createStatusEmbed(interaction.user.id)
    view = infosButtons()  
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)