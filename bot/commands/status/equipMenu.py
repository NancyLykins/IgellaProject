import discord
from asyncio import sleep
from commands.sql.character.update.updateBody import updateBody
from commands.sql.character.update.updateBuffs import updateBuffs
from commands.sql.character.update.updateHand import updateHand
from commands.sql.effects.saveCharacterEffect import saveCharacterEffect
from commands.sql.itens.update.updateItensInInventary import updateItensInInventary

from commands.sql.itens.removeItensInInventary import removeItensInInventary

from commands.sql.itens.select.takeEquipItens import takeEquipItens
from commands.sql.itens.select.takeEquipSlot import takeEquipSlot
from commands.sql.itens.select.takeItem import takeItem
from commands.sql.itens.select.takeItemQuant import takeItemQuant
trigget = 0

async def equipMenu(interaction: discord.Interaction):
    global trigget
    playerId = interaction.user.id
    if trigget == 0:
        trigget += 1
        await interaction.response.edit_message(embed=createEquipMenuEmbed(playerId), view=createEquipMenuView(playerId))
    else:
        await interaction.message.delete()
        msg = await interaction.channel.send(">>> Item equipado com sucesso")
        await sleep(5)
        await msg.delete()

async def equipThisItem(interaction: discord.Interaction):
    global trigget 
    try:
       await interaction.response.send_message()   
    except:
       pass
    
    result = takeItem(interaction.data["custom_id"])
    itemId = result[0]
    playerId = interaction.user.id
    slot = result[7]
    if(slot[-1] == "H"):
        handSlots = takeEquipSlot(playerId, "Hands", slot)
        handOne = handSlots[0]
        handTwo = handSlots[1]
        if(slot == "twoH" and takeEquipSlot(playerId, "Hands", "leftH") == None and takeEquipSlot(playerId, "Hands", "rightH") == None):
            updateHand(playerId, "leftH", itemId)
            updateHand(playerId, "rightH", itemId)
            await removeItem(interaction, playerId, itemId)
            await giveBonus(interaction, interaction.user.id, result[5])
            
        elif(slot != "towH" and handOne == None or handTwo == None):
            updateHand(playerId, slot, itemId)
            await removeItem(interaction, playerId, itemId)
            await giveBonus(interaction, interaction.user.id, result[5])
        
        else:
            await notInterupt(interaction)
            msg = await interaction.channel.send(">>> Você já tem um item equipado")
            await sleep(5)
            await msg.delete()
    else:
        if(takeEquipSlot(playerId, "Body", slot)[0] == None):
            updateBody(playerId, slot, itemId)
            await removeItem(interaction, playerId, itemId)
            await giveBonus(interaction, interaction.user.id, result[5])
        else:
            await notInterupt(interaction)
            msg = await interaction.channel.send(">>> Você já tem um item equipado")
            await sleep(5)
            await msg.delete()
    trigget = 0
    
async def notInterupt(interaction):
    try:
        await interaction.response.send_message()   
    except:
        pass
    
async def removeItem(interaction, playerId, itemId):
    await notInterupt(interaction)
    quant = int(takeItemQuant(playerId, itemId)) - 1
                
    if(quant <= 0):    
        removeItensInInventary(playerId, itemId)
    else:
        updateItensInInventary(playerId, itemId, quant)
    await equipMenu(interaction)
    
def createEquipMenuEmbed(playerId):
    embed = discord.Embed(
        title="Qual item deseja equipar?"
    )
    
    for item in takeEquipItens(playerId):
        embed.add_field(name="", value=f"{item[2]} {item[1].title()}: {item[3]}", inline=False)
    return embed

def createEquipMenuView(playerId):
    view = discord.ui.View()
    for item in takeEquipItens(playerId):
        button = discord.ui.Button(label=item[1].title(), style=discord.ButtonStyle.primary)
        button.callback = equipThisItem
        button.custom_id = str(item[0])
        view.add_item(button)
    return view
        
async def giveBonus(interaction, characterId, bonus):
    allBonusList = bonus[1:].split("-")
    for element in allBonusList:
        buff = element.split(":")
        if(buff[0] == 'effect'):
            roleId = int(buff[1].split("&")[1][:-1])
            role = discord.utils.get(interaction.guild.roles, id=roleId)
            await interaction.user.add_roles(role)
            saveCharacterEffect(characterId, roleId, 9999)
        else:
            updateBuffs(characterId, buff[0], int(buff[1]))