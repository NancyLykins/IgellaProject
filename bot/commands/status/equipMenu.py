import discord, aiohttp, os, asyncio
from dotenv import load_dotenv
from asyncio import sleep
load_dotenv()
url = os.getenv("API_URL")
header = {'Content-type': 'application/json'}
trigget = 0

async def equipMenu(interaction: discord.Interaction):
    global trigget
    id = interaction.user.id
    embed, view = await createEquipMenu(id)
    await interaction.response.edit_message(embed=embed, view=view)


async def equipThisItem(interaction: discord.Interaction):
    global trigget
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}/itens/{interaction.data['custom_id']}") as response:
            data = await response.json()
            item = data[0]
            itemId = item['rowId']
            id = interaction.user.id
            slot = item['slot']

    if slot[-1] == "H":
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{url}/characters/{id}/hands") as response:
                handSlots = await response.json()
                try:
                    handOne = handSlots["rowId"]
                except:
                    handOne = None
                try:
                    handTwo = handSlots["rowId"]
                except:
                    handTwo = None                   
                
                if slot == "twoH" and handOne is None and handTwo is None:
                    tasks = [
                        session.patch(f"{url}/characters/{id}/hands/{itemId}"),
                        session.patch(f"{url}/characters/{id}/hands/{itemId}"),
                        session.delete(f"{url}/characters/{id}/inventary/{itemId}")
                    ]
                    await asyncio.gather(*tasks)
                    await giveBonus(interaction, interaction.user.id, item['action'])
                    await interaction.response.edit_message(content="Item equipado com sucesso", view=None, embed=None)
                elif slot != "towH" and (handOne is None or handTwo is None):
                    tasks = [
                        session.patch(f"{url}/characters/{id}/hands/{itemId}"),
                        session.delete(f"{url}/characters/{id}/inventary/{itemId}")
                    ]
                    await asyncio.gather(*tasks)
                    await giveBonus(interaction, interaction.user.id, item['action'])        
                    await interaction.response.edit_message(content="Item equipado com sucesso", view=None, embed=None)
                else:
                    msg = await interaction.response.edit_message(content=">>> Você já tem um item equipado", view=None, embed=None)

    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{url}/characters/{id}/equips/{slot}") as response:
                item = (await response.json())[0][slot]
                if item is None or item == "None":
                    response = await session.get(f"{url}/itens/{itemId}")
                    action = (await response.json())[0]["action"]
                    tasks = [
                        session.patch(f"{url}/characters/{id}/equips/{slot}/{itemId}"),
                        session.delete(f"{url}/characters/{id}/inventary/{itemId}")
                    ]
                    await interaction.response.edit_message(content=">>> Item equipado com sucesso", embed=None, view=None)
                    await asyncio.gather(*tasks)
                    await giveBonus(interaction, interaction.user.id, action)
                else:
                    await interaction.response.send_message(">>> Você já tem um item equipado", ephemeral=True)
        trigget = 0

    
   
async def createEquipMenu(id):
    embed = discord.Embed(
        title="Qual item deseja equipar?"
    )
    view = discord.ui.View()

    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}/characters/{id}/inventary/equipable") as response:
            itens = await response.json()
            for item in itens:
                itemName = item["name"].title()
                embed.add_field(name="", value=f"{item['emoji']} {itemName}: {item['quant']}", inline=False)
                button = discord.ui.Button(label=itemName, style=discord.ButtonStyle.primary)
                button.callback = equipThisItem
                button.custom_id = str(item['itemId'])
                view.add_item(button)

    return embed, view
        
async def giveBonus(interaction, id, bonus):
    allBonusList = bonus[1:].split("-")
    async with aiohttp.ClientSession() as session:
        for element in allBonusList:
            buff = element.split(":")
            if buff[0] == 'effect':
                roleId = int(buff[1].split("&")[1][:-1])
                role = discord.utils.get(interaction.guild.roles, id=roleId)
                await interaction.user.add_roles(role)
                effect = {
                    "effectId": roleId,
                    "time": "99999"
                }
                await session.post(f"{url}/characters/{id}/effects", json=effect, headers=header)
            elif(buff != ['']):
                buff = {
                    buff[0]: f"+{buff[1]}"
                }
                await session.patch(f"{url}/characters/{id}/status", json=buff, headers=header)
            