from typing import Optional
import discord
from Commands.newObject.createObjects.waitForMessage import waitForMessage
from Commands.sql.itens.saveItem import saveItem
from Commands.newObject.createObjects.askItemInfos.askItemBuff import askItemBuff


class partBodyButtons(discord.ui.View):
    def __init__(self, client, itemInfos):
        super().__init__(timeout=120)
        self.value = None
        self.client = client
        self.itemInfos = itemInfos
        
    @discord.ui.button(label="Vestível", style=discord.ButtonStyle.primary)
    async def wearable(self, interaction, button):
        bodyParts = {
            "head": "Cabeça",
            "chest": "Tronco",
            "legs": "Perna",
            "feets": "Pés"
        }
        view = discord.ui.View()
        async def setBodyPart(interaction: discord.Interaction):
            await interaction.message.delete()
            itemInfos = self.itemInfos
            itemInfos["slot"] = interaction.data["custom_id"]
            await askItemBuff(interaction, self.client, itemInfos)

        
        for bodyPart in list(bodyParts.keys()):
            button = discord.ui.Button(label=bodyParts[bodyPart], style=discord.ButtonStyle.primary)
            button.custom_id = bodyPart
            button.callback = setBodyPart
            view.add_item(button)
        await interaction.response.edit_message(content=">>> Onde se veste esse item?" ,view=view)
        
    @discord.ui.button(label="Manuseavel", style=discord.ButtonStyle.primary)
    async def manegeable(self, interaction, button):
        handType = {
            "oneH": "Uma Mão",
            "twoH": "Duas Mãos"
        }
        view = discord.ui.View()
        async def setHandType(interaction: discord.Interaction):
            await interaction.message.delete()
            itemInfos = self.itemInfos
            itemInfos["slot"] = interaction.data["custom_id"]
            await askItemBuff(interaction, self.client, itemInfos)
        
        for type in list(handType.keys()):
            button = discord.ui.Button(label=handType[type], style=discord.ButtonStyle.primary)
            button.callback = setHandType
            button.custom_id = type
            view.add_item(button)
            
        await interaction.response.edit_message(content=">>> Com quantas segura esse item?", view=view)


async def askItemAction(ctx, client, itemInfos):
    itemType = itemInfos["type"]

    match itemType:
        case "usable":
            efeito = await waitForMessage(ctx, client, "Qual o efeito que ele da?\nMencione o cargo do efeito", 180)
            itemInfos["action"] = efeito
            
            def check(message):
                try:
                    messageContent = int(message.content)
                    return message.channel == ctx.channel and message.author == ctx.author and isinstance(messageContent, int)
                except:
                    return False
            
            msg = await ctx.send(">>> Qual a duração do efeito em turnos?")
            duration = await client.wait_for("message", check=check, timeout=120)
            await msg.delete()
            await duration.delete()
            itemInfos["time"] = duration.content
            saveItem(itemInfos)

        case "equipable":
            await ctx.send(">>> Qual a função desse equipamento?", view=partBodyButtons(client, itemInfos))

        case _:
            saveItem(itemInfos)
