import discord
from discord.ext import commands
from discord import app_commands

from commands.status.showStatus import showStatus
from commands.character.healCharacter import healCharacter

class characterCogs(commands.Cog):
    def __init__(self, client: discord.client):
        self.client=client
    
    @app_commands.command(name="status", description="Mostra as informações do seu personagem")
    async def status(self, interaction: discord.Interaction):
        await showStatus(interaction)
        
    @app_commands.command(name="heal", description="Cura uma certa quantidade de vida de um personagem")
    @app_commands.describe(player="Quem deve ser curado?")
    @app_commands.describe(life="Quanto de vida deve ser restaurado?")
    async def heal(self, interaction, player: discord.Member, life: int):
        await healCharacter(interaction, player, life)
        
async def setup(client: discord.Client) -> None:
    await client.add_cog(characterCogs(client))