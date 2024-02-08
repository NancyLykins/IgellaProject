import discord
from discord import app_commands
from discord.ext import commands
from commands.utils.clear import clear

class utilsCogs(commands.Cog):
    def __init__(self, client: discord.client):
        self.client = client
        
    @app_commands.command(name="clear")
    @app_commands.describe(limit="Quantas mensagens deseja apagar")
    async def clear(self, interaction: discord.Interaction, limit: str):
        await clear(interaction, limit)

      
async def setup(client: discord.Client) -> None:
    await client.add_cog(utilsCogs(client))