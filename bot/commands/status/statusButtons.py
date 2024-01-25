from typing import Optional
import discord
from .statusEmbeds.bodyEquipamentEmbed import bodyEquipamentEmbed
from .statusEmbeds.handEquipamentEmbed import handEquipamentEmbed
from .statusEmbeds.infosEmbed import infosEmbed
from .statusEmbeds.skillsEmbed import skillsEmbed
from commands.status.showInventaryEmbed import showInventaryEmbed
from commands.status.statusEmbeds.equipedArmoEmbed import equipedArmoEmbed
from commands.status.statusEmbeds.equipedHandsEmbed import equipedHandsEmbed
from commands.status.statusEmbeds.abilityEmbed import abilityEmbed

class equipamentsButtons(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Status", style=discord.ButtonStyle.success)
    async def menuStatisticas(self, interaction, button):
        embed = await infosEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=infosButtons())

    @discord.ui.button(label="Mãos", style=discord.ButtonStyle.secondary)
    async def handEquip(self, interaction, button):
        embed = await handEquipamentEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=handsButtons())

    @discord.ui.button(label="Desequipar", style=discord.ButtonStyle.red)
    async def desequipBody(self, interaction, button):
        embed, view = equipedArmoEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=view)

class handsButtons(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Status", style=discord.ButtonStyle.success)
    async def menuStatisticas(self, interaction, button):
        embed = await infosEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=infosButtons())

    @discord.ui.button(label="Corpo", style=discord.ButtonStyle.secondary)
    async def bodyEquip(self, interaction, button):
        embed = await bodyEquipamentEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=equipamentsButtons())

    @discord.ui.button(label="Desequipar", style=discord.ButtonStyle.red)
    async def desequipBody(self, interaction, button):
        embed, view = equipedHandsEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=view)

class skillsButton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        
    @discord.ui.button(label="Status", style=discord.ButtonStyle.success)
    async def menuStatisticas(self, interaction, button):
        embed = await infosEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=infosButtons())
            
class infosButtons(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        
    @discord.ui.button(label="Equi", style=discord.ButtonStyle.blurple)
    async def menuEquipamentos(self, interaction, button):
        embed = await bodyEquipamentEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=equipamentsButtons())

    @discord.ui.button(label="Inv", style=discord.ButtonStyle.danger)
    async def menuInventario(self, interaction, button):
        await showInventaryEmbed(interaction)
        
    @discord.ui.button(label="Pericias", style=discord.ButtonStyle.gray)
    async def menuPericias(self, interaction, button):
        embed = await skillsEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=skillsButton())

    @discord.ui.button(label="Habilidades", style=discord.ButtonStyle.green)
    async def menuHabilidades(self, interaction, button):
        embed = await abilityEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=showAbility())

class showAbility(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        
    @discord.ui.button(label="Status", style=discord.ButtonStyle.success)
    async def menuStatisticas(self, interaction, button):
        embed = await infosEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=infosButtons())