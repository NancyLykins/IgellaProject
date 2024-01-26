import discord, requests, os
from dotenv import load_dotenv


import commands.status.statusButtons
from commands.status.embeds.createStatusEmbed import createStatusEmbed
from commands.status.useMenu import useMenu
# from commands.status.equipMenu import equipMenu

load_dotenv()
url = os.getenv("API_URL")

dinheiro = {
    "img": "",
    "quant": ""
}
has = {
    "equipable": False,
    "usable": False
}

async def createInventaryEmbed(id):
    embed = discord.Embed(
        title= "Inventário",
        colour= 119911 
    )
    print(embed)
    response = requests.get(f"{url}/characters/{id}/inventary")
    inventary = response.json()
    for item in inventary:
        if(item["name"] != "moeda"):
            match item["type"]:
                case "equipable":
                    has["equipable"] = True
                case "usable":
                    has["usable"] = True
                             
            embed.add_field(name="", value=f"{item['emoji']} {item['name'].title()}: {item['quant']}", inline=False)
        else:
            dinheiro["img"] = item['emoji']
            dinheiro["quant"] = f"{item['quant']}¤"
    
    embed.add_field(name="", value=f"{dinheiro['img']} Dinheiro: {dinheiro['quant']}")
    return embed, has

async def showInventaryEmbed(interaction: discord.Interaction):
    view = discord.ui.View(timeout=1800)
    embed, has = await createInventaryEmbed(interaction.user.id)
    async def menuStatisticas(interaction: discord.Interaction):
        embed = await createStatusEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=commands.status.statusButtons.infosButtons())
    
    statusButton = discord.ui.Button(label="Status", style=discord.ButtonStyle.success)
    statusButton.callback = menuStatisticas
    view.add_item(statusButton)
    
    for element in has:
        if(element == 'equipable' and has[element] == True):
            button = discord.ui.Button(label="Equipar", style=discord.ButtonStyle.primary)
            button.callback = equipMenu
            view.add_item(button)
            
        if(element == 'usable' and has[element] == True):
            button = discord.ui.Button(label="Usar", style=discord.ButtonStyle.red)
            button.callback = useMenu
            view.add_item(button)
    
    await interaction.response.edit_message(embed=embed, view=view)