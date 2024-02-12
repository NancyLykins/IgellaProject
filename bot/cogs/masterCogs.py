import discord
from discord import app_commands
from discord.ext import commands
from commands.character.giveItem import giveItem

class masterCogs(commands.Cog):
    def __init__(self, client: discord.client):
        self.client = client
        
    @app_commands.command(name="give")
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(player="Qual o personagem que ira receber o item?")
    @app_commands.describe(item="Qual item sera dado ao personagem?")
    @app_commands.describe(amount="Quantos itens serão dados?")
    async def give(self, interaction: discord.Interaction, player: discord.Member, item: str, amount: int):
        await giveItem(interaction, player, item, amount)
        
    @app_commands.command(name="summon")
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(monster="Qual criatura deseja invocar")
    async def summon(self, interaction, monster: str):
        print(monster)

async def setup(client: discord.Client) -> None:
    await client.add_cog(masterCogs(client))
    