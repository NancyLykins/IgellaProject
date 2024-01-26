import discord

from commands.status.embeds.createStatusEmbed import createStatusEmbed
from commands.status.embeds.createHandsEmbed import createHandsEmbed
from commands.status.embeds.createEquipsEmbed import createEquipsEmbed
from commands.status.embeds.createInventaryEmbed import showInventaryEmbed
from commands.status.embeds.createSkillsEmbed import createSkillsEmbed
from commands.status.embeds.createAbilitysEmbed import createAbilitysEmbed


class equipamentsButtons(discord.ui.View):
    def _init_(self):
        super()._init_()
        self.value = None

    @discord.ui.button(label="Status", style=discord.ButtonStyle.success)
    async def menuStatisticas(self, interaction, button):
        embed = await createStatusEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=infosButtons())

    @discord.ui.button(label="Mãos", style=discord.ButtonStyle.secondary)
    async def handEquip(self, interaction, button):
        embed = await createHandsEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=handsButtons())

    @discord.ui.button(label="Desequipar", style=discord.ButtonStyle.red)
    async def desequipBody(self, interaction, button):
        embed, view = equipedArmoEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=view)

class handsButtons(discord.ui.View):
    def _init_(self):
        super()._init_()
        self.value = None

    @discord.ui.button(label="Status", style=discord.ButtonStyle.success)
    async def menuStatisticas(self, interaction, button):
        embed = await createStatusEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=infosButtons())

    @discord.ui.button(label="Corpo", style=discord.ButtonStyle.secondary)
    async def bodyEquip(self, interaction, button):
        embed = await createEquipsEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=equipamentsButtons())

    @discord.ui.button(label="Desequipar", style=discord.ButtonStyle.red)
    async def desequipBody(self, interaction, button):
        embed, view = equipedHandsEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=view)

class skillsButton(discord.ui.View):
    def _init_(self):
        super()._init_()
        self.value = None
        
    @discord.ui.button(label="Status", style=discord.ButtonStyle.success)
    async def menuStatisticas(self, interaction, button):
        embed = await createStatusEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=infosButtons())
            
class infosButtons(discord.ui.View):
    def _init_(self):
        super()._init_()
        self.value = None
        
    @discord.ui.button(label="Equi", style=discord.ButtonStyle.blurple)
    async def menuEquipamentos(self, interaction, button):
        embed = await createEquipsEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=equipamentsButtons())

    @discord.ui.button(label="Inv", style=discord.ButtonStyle.danger)
    async def menuInventario(self, interaction, button):
        await showInventaryEmbed(interaction)
        
    @discord.ui.button(label="Pericias", style=discord.ButtonStyle.gray)
    async def menuPericias(self, interaction, button):
        embed = await createSkillsEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=skillsButton())

    @discord.ui.button(label="Habilidades", style=discord.ButtonStyle.green)
    async def menuHabilidades(self, interaction, button):
        embed = await createAbilitysEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=showAbility())


class showAbility(discord.ui.View):
    def _init_(self):
        super()._init_()
        self.value = None
        
    @discord.ui.button(label="Status", style=discord.ButtonStyle.success)
    async def menuStatisticas(self, interaction, button):
        embed = await createStatusEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=infosButtons())