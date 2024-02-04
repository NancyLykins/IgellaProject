import discord, os, requests
from dotenv import load_dotenv
load_dotenv()
url = os.getenv('API_URL')
header = {'Content-type': 'application/json'}

async def unequipItem(interaction: discord.Interaction):
    itemId = int(interaction.data["custom_id"])
    playerId = interaction.user.id
    effectBuff = {}
    respose = requests.get(f"{url}/itens/{itemId}")
    itemSlot = respose.json()[0]["slot"]
    requests.patch(f"{url}/characters/{playerId}/equips/{itemSlot}/{None}")
    requests.post(f"{url}/characters/{playerId}/inventary/{itemId}")
    response = requests.get(f"{url}/itens/{itemId}")
    action = response.json()[0]["action"]
    allBonusList = action[1:].split("-")
    for element in allBonusList:
        buff = element.split(":")
        if(buff[0] == 'effect'):
            roleId = int(buff[1].split("&")[1][:-1])
            role = discord.utils.get(interaction.guild.roles, id=roleId)
            requests.delete(f"{url}/characters/{playerId}/effects/{roleId}")
            response = requests.get(f"{url}/effects/{roleId}")
            effect = response.json()[0]
            effectBuff["agilidadeBuff"] = effect["agiBuff"]
            effectBuff["forcaBuff"] = effect["forBuff"]
            effectBuff["inteligenciaBuff"] = effect["intBuff"]
            effectBuff["presencaBuff"] = effect["preBuff"]
            effectBuff["vigorBuff"] = effect["vigBuff"]
            effectKeys = list(effectBuff.keys())
            for effect in effectKeys:
                if effectBuff[effect] != 0:
                    body = {
                        effect: effectBuff[effect]
                    }
                    requests.patch(f"{url}/characters/{id}/effects", headers=header, json=body)
            await interaction.user.remove_roles(role)
        else:
            body = {
                buff[0]: f"-{buff[1]}"
            }
            requests.patch(f"{url}/characters/{id}/effects", headers=header, json=body)
    
    
    await interaction.response.edit_message(embed=None, content=">>> Desequipado com sucesso", view=None)
    

def equipedArmoEmbed(id):
    response = requests.get(f"{url}/characters/{id}/equips")
    equips = response.json()[0]
    if(equips != [] ^ isinstance(equips, type(None))):
        embed = discord.Embed(
            title="Qual item quer desequipar?",
            colour = 128743
        )
        view = discord.ui.View(timeout=180)
        response = requests.get(f"{url}/characters/{id}/armor")
        equips = response.json()
        for item in equips:
            itemId = item["rowId"]
            itemName = item["name"].title()
            itemEmoji = item["emoji"]
            
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