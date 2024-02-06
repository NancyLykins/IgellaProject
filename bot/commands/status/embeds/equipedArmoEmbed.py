import discord, os, aiohttp
from dotenv import load_dotenv
load_dotenv()
url = os.getenv('API_URL')
header = {'Content-type': 'application/json'}

async def unequipItem(interaction: discord.Interaction):
    itemId = int(interaction.data["custom_id"])
    id = interaction.user.id
    effectBuff = {}
    async with aiohttp.ClientSession() as session:
        response = await session.get(f"{url}/itens/{itemId}")
        itemSlot = (await response.json())[0]["slot"]
        response = await session.patch(f"{url}/characters/{id}/equips/{itemSlot}/{None}")
        await session.post(f"{url}/characters/{id}/inventary/{itemId}")
        response = await session.get(f"{url}/itens/{itemId}")
        action = (await response.json())[0]["action"]
        allBonusList = action[1:].split("-")
        for element in allBonusList:
            buff = element.split(":")
            if(buff[0] == 'effect'):
                roleId = int(buff[1].split("&")[1][:-1])
                role = discord.utils.get(interaction.guild.roles, id=roleId)
                await session.delete(f"{url}/characters/{id}/effects/{roleId}")
                response = await session.get(f"{url}/effects/{roleId}")
                effect = (await response.json())[0]
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
                        await session.patch(f"{url}/characters/{id}/effects", headers=header, json=body)
                await interaction.user.remove_roles(role)
            else:
                body = {
                    buff[0]: f"-{buff[1]}"
                }
                await session.patch(f"{url}/characters/{id}/effects", headers=header, json=body)
    await interaction.response.edit_message(embed=None, content=">>> Desequipado com sucesso", view=None)
    

async def equipedArmoEmbed(id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}/characters/{id}/equips") as response:
            equips = await response.json()
        if(equips != []):
            embed = discord.Embed(
                title="Qual item quer desequipar?",
                colour = 128743
            )
            view = discord.ui.View(timeout=180)
            async with session.get(f"{url}/characters/{id}/armor") as response:
                equips = await response.json()
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