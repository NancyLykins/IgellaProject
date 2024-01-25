import discord
from Commands.sql.character.select.equip.takeEquipArmo import takeEquipArmo
from Commands.sql.character.remove.equip.removeBodyEquip import removeBodyEquip
from Commands.sql.itens.select.takeItem import takeItem
from Commands.sql.character.select.equip.takeBodyEquip import takeBodyEquip
from Commands.sql.itens.select.takeItemAction import takeItemAction
from Commands.sql.character.remove.removeEffect import removeEffect
from Commands.sql.character.remove.resetBuffs import resetBuffs
from Commands.sql.effects.select.takeEffectBuff import takeEffectBuff

async def unequipItem(interaction: discord.Interaction):
    id = int(interaction.data["custom_id"])
    characterId = interaction.user.id
    item = takeItem(id)
    effectBuff = {}
    removeBodyEquip(interaction.user.id, id, item[7])
    action = takeItemAction(id)
    allBonusList = action[1:].split("-")
    for element in allBonusList:
        buff = element.split(":")
        if(buff[0] == 'effect'):
            roleId = int(buff[1].split("&")[1][:-1])
            role = discord.utils.get(interaction.guild.roles, id=roleId)
            removeEffect(characterId, roleId)
            effect = takeEffectBuff(role.id)
            effectBuff["agilidadeBuff"] = effect[0]
            effectBuff["forcaBuff"] = effect[1]
            effectBuff["inteligenciaBuff"] = effect[2]
            effectBuff["presencaBuff"] = effect[3]
            effectBuff["vigorBuff"] = effect[4]
            effectKeys = list(effectBuff.keys())
            for effect in effectKeys:
                if effectBuff[effect] != 0:
                    resetBuffs(characterId, effect, effectBuff[effect])
            await interaction.user.remove_roles(role)
        else:
            resetBuffs(characterId, buff[0], int(buff[1]))
    
    
    await interaction.response.edit_message(embed=None, content=">>> Desequipado com sucesso", view=None)
    

def equipedArmoEmbed(playerId):
    if(takeBodyEquip(playerId) != []):
        embed = discord.Embed(
            title="Qual item quer desequipar?",
            colour = 128743
        )
        view = discord.ui.View(timeout=180)
        for item in takeEquipArmo(playerId):
            itemId = item[0]
            itemName = item[1].title()
            itemEmoji = item[2]
            
            embed.add_field(name=f"{itemName} {itemEmoji}", value="", inline=False)
            button = discord.ui.Button(label=itemName, style=discord.ButtonStyle.primary)
            button.custom_id = str(itemId)
            button.callback = unequipItem
            view.add_item(button)
    else:
        embed = discord.Embed(
            title="Você não tem nenhum item equipado",
            colour = 128743
        )
        view = None
            
    return (embed, view)
        
        
        