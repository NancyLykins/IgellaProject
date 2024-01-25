from typing import Optional
import discord
from Commands.sql.character.deleteChar import deleteChar

class confirmButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=120)
        self.value = None
        
    @discord.ui.button(label="Sim", style=discord.ButtonStyle.green)
    async def yes(self, interaction, button):
        try:
            await deleteChar(interaction.user.id)
            await interaction.response.edit_message("Personagem excluido com sucesso")
        except:
            await interaction.response.edit_message(f"Nenhum personagem encontrado para {interaction.user}")
        
    @discord.ui.button(label="Não", style=discord.ButtonStyle.red)
    async def no(self, interaction, button):
        await interaction.response.edit_message(content="Exclusão cancelada", view=None)

async def deleteCharacter(interaction: discord.Interaction):
    await interaction.response.send_message("Realmente deseja excliur seu personagem", view=confirmButtons(), ephemeral=True)