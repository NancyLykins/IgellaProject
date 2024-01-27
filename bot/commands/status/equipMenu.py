import discord, requests, os
from dotenv import load_dotenv
from asyncio import sleep
load_dotenv()
url = os.getenv("API_URL")
header = {'Content-type': 'application/json'}
trigget = 0

async def equipMenu(interaction: discord.Interaction):
    global trigget
    id = interaction.user.id
    if trigget == 0:
        trigget += 1
        embed, view = createEquipMenu(id)
        await interaction.response.edit_message(embed=embed, view=view)
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
    
    response = requests.get(f"{url}/itens/{interaction.data['custom_id']}")
    item = response.json()[0]
    itemId = item['itemId']
    id = interaction.user.id
    slot = item['slot']
    if(slot[-1] == "H"):
        response = requests.get(f"{url}/characters/{id}/hands")
        handSlots = response.json()
        handOne = handSlots[0] or None
        handTwo = handSlots[1] or None
        if(slot == "twoH" and handOne is None and handTwo is None):
            requests.patch(f"{url}/characters/{id}/hands/{itemId}")
            requests.patch(f"{url}/characters/{id}/hands/{itemId}")
            requests.delete(f"{url}/characters/{id}/inventary/{itemId}")
            await giveBonus(interaction, interaction.user.id, item['action'])
            
        elif(slot != "towH" and handOne == None or handTwo == None):
            requests.patch(f"{url}/characters/{id}/hands/{itemId}")
            requests.delete(f"{url}/characters/{id}/inventary/{itemId}")
            await giveBonus(interaction, interaction.user.id, item['action'])
        
        else:
            await notInterupt(interaction)
            msg = await interaction.channel.send(">>> Você já tem um item equipado")
            await sleep(5)
            await msg.delete()
    else:
        response = requests.get(f"{url}/characters/equips/{slot}")
        item = response.json()[0]
        if(item is not None):
            requests.patch(f"{url}/characters/equips/{slot}/{itemId}")
            requests.delete(f"{url}/characters/{id}/inventary/{itemId}")
            await giveBonus(interaction, interaction.user.id, item['action'])
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
    
async def removeItem(interaction, id, itemId):
    await notInterupt(interaction)
    response = requests.get(f"{url}/characters/{id}/inventary/{itemId}")
    quant = int(response.json()[0]) - 1
                
    if(quant <= 0):
        requests.delete(f"{url}/characters/{id}/inventary/{itemId}")
        await interaction.message.delete()
    else:
        body = {"quant": quant}
        requests.patch(f"{url}/characters/{id}/inventary/{itemId}", json=body, headers=header)
    await equipMenu(interaction)
    
def createEquipMenu(id):
    embed = discord.Embed(
        title="Qual item deseja equipar?"
    )
    view = discord.ui.View()
    response = requests.get(f"{url}/characters/{id}/inventary/equipable")
    itens = response.json()
    for item in itens:
        itemName = item["name"].title()
        embed.add_field(name="", value=f"{item['emoji']} {itemName}: {item['quant']}", inline=False)
        button = discord.ui.Button(label=itemName, style=discord.ButtonStyle.primary)
        button.callback = equipThisItem
        button.custom_id = str(item['itemId'])
        view.add_item(button)
    
    return embed, view
        
async def giveBonus(interaction, characterId, bonus):
    allBonusList = bonus[1:].split("-")
    for element in allBonusList:
        buff = element.split(":")
        if(buff[0] == 'effect'):
            roleId = int(buff[1].split("&")[1][:-1])
            role = discord.utils.get(interaction.guild.roles, id=roleId)
            await interaction.user.add_roles(role)
            effect = {
                "effectId": roleId,
                "time": "99999"
            }
            requests.post(f"{url}/characters/effects", json=effect, headers=header)
        else:
            buff = {
                buff[0]: f"+{buff[1]}"
            }
            requests.patch(f"{url}/characters/{id}/status", json=buff, headers=header)