import discord, requests, os
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
        response = requests.get(f"{url}/itens/{interaction.data['custom_id']}")
        item = response.json()[0]
        time = item['type']
        roleId = item['action']
        roleId = int(roleId.split("&")[1][:-1])
        userHasRole = interaction.user.get_role(roleId)
        role = discord.utils.get(interaction.guild.roles, id=roleId)
        if(userHasRole == None):
            await interaction.user.add_roles(role)
            itemId = item['rowId']
            quant = quantidade[itemId] - 1
            if(quant <= 0):
                requests.delete(f"{url}/characters/{id}/inventary/{itemId}")
                await interaction.message.delete()
            else:
                body = {"quant": quant}
                requests.patch(f"{url}/characters/{id}/inventary/{itemId}", json=body, headers=header)
                await useMenu(interaction)
            
            effect = {
                "effectId": roleId,
                "time": time
            }
            requests.post(f"{url}/characters/{id}/effects", json=effect, headers=header)
            

        else:
            try:
                await interaction.response.send_message()
                
            except discord.errors.HTTPException:
                await interaction.channel.send(f"` Você já está sobre o efeito: {role} `")

    response = requests.get(f"{url}/characters/{id}/inventary/usable")
    useItens = response.json()
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
 