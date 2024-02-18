import discord
from discord import app_commands
from discord.ext import commands
from commands.utils.clear import clear
from commands.utils.sayText import sayText

class utilsCogs(commands.Cog):
    def __init__(self, client: discord.client):
        self.client = client
        
    @app_commands.command(name="clear")
    @app_commands.describe(limit="Quantas mensagens deseja apagar")
    async def clear(self, interaction: discord.Interaction, limit: str):
        await clear(interaction, limit)

    @app_commands.command(name="say")
    @app_commands.describe(message="Mensagem")
    @app_commands.default_permissions(administrator=True)
    async def say(self, interaction: discord.Interaction, message: str):
        await interaction.channel.send(message)
        await interaction.response.send_message("Mensagem enviada com sucesso" ,ephemeral=True)
        
    @app_commands.command(name="say_text")
    @app_commands.describe(title="Titulo do texto")
    @app_commands.describe(message="Mensagem do texto")
    @app_commands.describe(footer="Rodapé do texto")
    async def sayText(self, interaction: discord.Interaction, title: str, message: str, footer: str):
        await sayText(interaction, title, message, footer)

      
async def setup(client: discord.Client) -> None:
    await client.add_cog(utilsCogs(client))