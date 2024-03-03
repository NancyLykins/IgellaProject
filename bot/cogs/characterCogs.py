import discord
from discord.ext import commands
from discord import app_commands

from commands.status.showStatus import showStatus
from commands.character.characterLife import characterLife
from commands.character.characterMana import characterMana


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
        await characterLife(interaction, player, life, "+")
        
    @app_commands.command(name="damage", description="Causa uma certa quantidade de dano a um personagem")
    @app_commands.describe(player="Quem deve receber dano?")
    @app_commands.describe(life="Quanto de vida deve removida?")
    async def damage(self, interaction, player: discord.Member, life: int):
        await characterLife(interaction, player, life, "-")
        
    @app_commands.command(name="recovery", description="Restaura um certa quantidade de mana de um player")
    @app_commands.describe(player="Quem deve ter a mana restaurada?")
    @app_commands.describe(mana="Quanto de mana deve ser restaurada?")
    async def recovery(self, interaction, player: discord.Member, mana: int):
        await characterMana(interaction, player, mana, "+")
        
    @app_commands.command(name="spell", description="Remove uma certa quantidade de mana de um player")
    @app_commands.describe(player="Quem deve ter a mana removida?")
    @app_commands.describe(mana="Quanto de mana deve ser removida?")
    async def spell(self, interaction, player: discord.Member, mana: int):
        await characterMana(interaction, player, mana, "-")



async def setup(client: discord.Client) -> None:
    await client.add_cog(characterCogs(client))