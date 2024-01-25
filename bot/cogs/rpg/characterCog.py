import discord
from discord.ext import commands
from discord import app_commands
from commands.status.showStatus import showStatus
from commands.character.deleteCharacter import deleteCharacter

class characterCog(commands.Cog):
    def __init__(self, client: discord.client):
        self.client = client
        
    @app_commands.command(name="delete", description="Exclui um personagem existente")
    async def delete(self, interaction: discord.Interaction):
        await deleteCharacter(interaction)

    @app_commands.command(name="status", description="Mostra o menu do seu personagem")
    async def status(self, interaction: discord.Interaction):
        await showStatus(interaction)

async def setup(client: discord.Client) -> None:
    await client.add_cog(characterCog(client))
    