from typing import Optional
import discord
from Commands.newObject.createObjects.askItemInfos.askItemAction import askItemAction


class askItemType(discord.ui.View):
    def __init__(self, ctx, client, itemInfos):
        super().__init__(timeout=120)
        self.value = None
        self.ctx = ctx
        self.client = client
        self.itemInfos = itemInfos
        
    @discord.ui.button(label="Item", style=discord.ButtonStyle.primary)
    async def item(self, interaction, button):
        await end(self.ctx, interaction, self.client, self.itemInfos, "item")
        
    @discord.ui.button(label="Usavel", style=discord.ButtonStyle.primary)
    async def usavel(self, interaction, button):
        await end(self.ctx, interaction, self.client, self.itemInfos, "usable")
        
    @discord.ui.button(label="Equipavel", style=discord.ButtonStyle.primary)
    async def equipavel(self, interaction, button):
        await end(self.ctx, interaction, self.client, self.itemInfos, "equipable")

        
        
async def end(ctx, interaction, client, itemInfos, type):
    itemInfos["type"] = type
    await askItemAction(ctx, client, itemInfos)
    await interaction.message.delete()
