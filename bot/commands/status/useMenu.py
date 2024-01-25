import discord, requests
from commands.status.statusButtons import *
from commands.sql.itens.select.takeUseItens import takeUseItens
from commands.sql.itens.select.takeItem import takeItem
from commands.sql.itens.removeItensInInventary import removeItensInInventary
from commands.sql.itens.update.updateItensInInventary import updateItensInInventary
from commands.sql.effects.saveCharacterEffect import saveCharacterEffect
import commands.status.showInventaryEmbed


async def useMenu(interaction: discord.Interaction):
    playerId = interaction.user.id
    
    embed = discord.Embed(
        title = "Qual item deseja usar?",
        colour = 436519
    )
    view = discord.ui.View(timeout=1800)
    
    quantidade = {}
    
    async def useThisItem(interaction: discord.Interaction):
        result = takeItem(interaction.data["custom_id"])
        time = result[6]
        roleId = result[5]
        roleId = int(roleId.split("&")[1][:-1])
        userHasRole = interaction.user.get_role(roleId)
        role = discord.utils.get(interaction.guild.roles, id=roleId)
        if(userHasRole == None):
            await interaction.user.add_roles(role)
            itemId = result[0]
            quant = quantidade[itemId] - 1
            print(quant)
            if(quant <= 0):    
                removeItensInInventary(playerId, itemId)
                await interaction.message.delete()
            
            else:
                updateItensInInventary(playerId, itemId, quant)
                await useMenu(interaction)
            
            saveCharacterEffect(playerId, roleId, time)
            

        else:
            try:
                await interaction.response.send_message()
                
            except discord.errors.HTTPException:
                await interaction.channel.send(f"` Você já está sobre o efeito: {role} `")
    response = requests.get(f"http://localhost:5050/character/{playerId}/inventary")
    data = response.json()
    useItens = []
    for item in data:
        if item["type"] == "usable":
            useItens.append(item)
    for item in useItens:
        itemName = item[1].title()
        quantidade[item[0]] = item[3]
        embed.add_field(name="", value=f"{item["quant"]} {item["name"]}: {item[""]}", inline=False)
        
        button = discord.ui.Button(label=item["name"], style=discord.ButtonStyle.primary)
        button.callback = useThisItem
        button.custom_id = str(item[0])
        
        view.add_item(button)
        
    voltarButton = discord.ui.Button(label="Voltar", style=discord.ButtonStyle.red)
    voltarButton.callback = Commands.status.showInventaryEmbed.showInventaryEmbed
    view.add_item(voltarButton)
        
    await interaction.response.edit_message(embed=embed, view=view)
