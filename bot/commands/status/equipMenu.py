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
                handOne = handSlots[0] or None
                handTwo = handSlots[1] or None
                if slot == "twoH" and handOne is None and handTwo is None:
                    tasks = [
                        session.patch(f"{url}/characters/{id}/hands/{itemId}"),
                        session.patch(f"{url}/characters/{id}/hands/{itemId}"),
                        session.delete(f"{url}/characters/{id}/inventary/{itemId}")
                    ]
                    await asyncio.gather(*tasks)
                    await giveBonus(interaction, interaction.user.id, item['action'])
                    
                elif slot != "towH" and (handOne is None or handTwo is None):
                    tasks = [
                        session.patch(f"{url}/characters/{id}/hands/{itemId}"),
                        session.delete(f"{url}/characters/{id}/inventary/{itemId}")
                    ]
                    await asyncio.gather(*tasks)
                    await giveBonus(interaction, interaction.user.id, item['action'])        
                
                else:
                    msg = await interaction.channel.send(">>> Você já tem um item equipado")
                    await sleep(5)
                    await msg.delete()
    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{url}/characters/{id}/equips/{slot}") as response:
                item = (await response.json())[0][slot]
                if item is None or item == "None":
                    tasks = [
                        session.patch(f"{url}/characters/{id}/equips/{slot}/{itemId}"),
                        session.delete(f"{url}/characters/{id}/inventary/{itemId}")
                    ]
                    await interaction.response.edit_message(content=">>> Item equipado com sucesso", embed=None, view=None)
                    await asyncio.gather(*tasks)
                    await giveBonus(interaction, interaction.user.id, item['action'])
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
        
async def giveBonus(interaction, characterId, bonus):
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
                async with session.post(f"{url}/characters/effects", json=effect, headers=header):
                    pass
            else:
                buff = {
                    buff[0]: f"+{buff[1]}"
                }
                async with session.patch(f"{url}/characters/{id}/status", json=buff, headers=header):
                    pass