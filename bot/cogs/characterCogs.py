import discord
from discord.ext import commands
from discord import app_commands

from commands.status.showStatus import showStatus

class characterCogs(commands.Cog):
    def __init__(self, client: discord.client):
        self.client=client
    
    @app_commands.command(name="status", description="Mostra as informações do seu personagem")
    async def status(self, interaction: discord.Interaction):
        await showStatus(interaction)
        
        
async def setup(client: discord.Client) -> None:
    await client.add_cog(characterCogs(client))