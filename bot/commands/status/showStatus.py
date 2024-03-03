import discord, os, aiohttp
from commands.status.embeds.createStatusEmbed import createStatusEmbed
from commands.status.statusButtons import *
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")
header = {'Content-type': 'application/json'}
async def showStatus(interaction: discord.Interaction):
    embed = await createStatusEmbed(interaction.user.id)
    view = infosButtons()  
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}/characters/{interaction.user.id}") as response:
            data = (await response.json())[0]
    points = data["pontosRestantes"]
    
    async def upgrade(interaction: discord.Interaction):      
        view = discord.ui.View()
        attributes = ["agilidade", "forca", "inteligencia", "presenca", "vigor"]

        async def upAttr(interaction: discord.Interaction):
            attrName = interaction.data["custom_id"]
            body = {
                "pontosRestantes": "-1",
                attrName: "+1"
            }           
            async with aiohttp.ClientSession() as session:
                await session.patch(f"{url}/characters/{interaction.user.id}", json=body, headers=header)
                async with session.get(f"{url}/characters/{interaction.user.id}") as response:
                    data = (await response.json())[0]
            points = data["pontosRestantes"]
            embed = createEditAttrEmbed(points)
            try:
                if(points != 0):
                    await interaction.response.edit_message(embed=embed)
                else:
                    embed = await showStatus(interaction)
                    await interaction.response.edit_message(embed=embed, view=infosButtons)
            except discord.errors.InteractionResponded:
                pass
                
        
        for attr in attributes:
            label = attr[:3].upper()
            button = discord.ui.Button(label=label, style=discord.ButtonStyle.primary)
            button.custom_id = attr
            button.callback = upAttr
            view.add_item(button)
         
        async def finishUpdate(interaction: discord.Interaction):
            embed = await showStatus(interaction)
            view = infosButtons()
            view = createUpdateStatusButton(view, points, upgrade)
            await interaction.response.edit_message(embed=embed, view=view)
            
        button = discord.ui.Button(label="EXIT", style=discord.ButtonStyle.danger)
        button.callback = finishUpdate
        view.add_item(button)

        embed = createEditAttrEmbed(points)
        await interaction.response.edit_message(embed=embed, view=view)
  
    view = createUpdateStatusButton(view, points, upgrade)
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
  
def createEditAttrEmbed(points):
    embed = discord.Embed(
            title="Distribua seus pontos",
            colour=326754
        )
    embed.set_footer(text=f"Você tem {points} {'restante' if points == 1 else 'restantes'}")
    return embed

def createUpdateStatusButton(view, points, upgrade):
    if(points > 0):
        button = discord.ui.Button(label="UP STATUS", style=discord.ButtonStyle.green)
        button.custom_id = "upStatus"
        button.callback = upgrade
        view.add_item(button)
    return view