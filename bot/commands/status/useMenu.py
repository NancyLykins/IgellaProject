import discord, aiohttp, os, asyncio
import commands.status.embeds.createInventaryEmbed
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")
header = {'Content-type': 'application/json'}

async def useMenu(interaction: discord.Interaction):
    id = interaction.user.id
    
    embed = discord.Embed(
        title = "Qual item deseja usar?",
        colour = 436519
    )
    view = discord.ui.View(timeout=1800)
    
    quantidade = {}
    
    async def useThisItem(interaction: discord.Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{url}/itens/{interaction.data['custom_id']}") as response:
                item = await response.json()
                item = item[0]
            time = item['type']
            roleId = item['action']
            roleId = int(roleId.split("&")[1][:-1])
            userHasRole = interaction.user.get_role(roleId)
            role = discord.utils.get(interaction.guild.roles, id=roleId)
            if(userHasRole == None):
                await interaction.user.add_roles(role)
                itemId = item['rowId']
                quant = quantidade[itemId] - 1
                tasks = []
                if(quant <= 0):
                    tasks.append(session.delete(f"{url}/characters/{id}/inventary/{itemId}"))
                    await interaction.message.delete()
                else:
                    body = {"quant": quant}
                    tasks.append(session.patch(f"{url}/characters/{id}/inventary/{itemId}", json=body))
                    await useMenu(interaction)
                
                effect = {
                    "effectId": roleId,
                    "time": time
                }
                tasks.append(session.post(f"{url}/characters/{id}/effects", json=effect))
                await asyncio.gather(*tasks)            

            else:
                try:
                    await interaction.response.send_message()
                    
                except discord.errors.HTTPException:
                    await interaction.channel.send(f"` Você já está sobre o efeito: {role} `")

    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}/characters/{id}/inventary/usable") as response:
            useItens = await response.json()
            for item in useItens:
                itemName = item['name'].title()
                quantidade[item['itemId']] = item['quant']
                embed.add_field(name="", value=f"{item['emoji']} {itemName}: {item['quant']}", inline=False)               
                button = discord.ui.Button(label=itemName, style=discord.ButtonStyle.primary)
                button.callback = useThisItem
                button.custom_id = str(item['itemId'])               
                view.add_item(button)

    voltarButton = discord.ui.Button(label="Voltar", style=discord.ButtonStyle.red)
    voltarButton.callback = commands.status.embeds.createInventaryEmbed.showInventaryEmbed
    view.add_item(voltarButton)
        
    await interaction.response.edit_message(embed=embed, view=view)