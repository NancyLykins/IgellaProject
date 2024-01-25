import discord, requests
from commands.status.statusEmbeds.infosEmbed import infosEmbed
from commands.status.statusButtons import *
from commands.sql.character.update.updateAttr import updateAttr
from commands.sql.character.update.updatePoints import updatePoints

async def showStatus(interaction):
    playerId = interaction.user.id
    view = infosButtons()  
    embed = await infosEmbed(playerId)
    response = requests.get(f"http://localhost:5050/character/{playerId}")
    data = response.json()[0]  
    points = data["pontosRestantes"]
    
    async def upgrade(interaction: discord.Interaction):      
        view = discord.ui.View()
        attributes = ["agilidade", "forca", "inteligencia", "presenca", "vigor"]
        
        async def upAttr(interaction: discord.Integration):
            attrName = interaction.data["custom_id"]
            
            attr = data[attrName]
            attr += 1
            
            points = data["pontosRestantes"]
            points -= 1
            updateAttr(playerId, attrName, attr)
            updatePoints(playerId, points)
            embed = createEditAttrEmbed(points)
            if(points != 0):
                await interaction.response.edit_message(embed=embed, ephemeral=True)
            else:
                embed = await infosEmbed(playerId)
                await interaction.message.delete()
        
        for attr in attributes:
            label = attr[:3].upper()
            button = discord.ui.Button(label=label, style=discord.ButtonStyle.primary)
            button.custom_id = attr
            button.callback = upAttr
            view.add_item(button)
               
        async def finishUpdate(interaction: discord.Interaction):
            embed = await infosEmbed(playerId)
            view = infosButtons()
            view = createUpdateStatusButton(view, points, upgrade)    
            await interaction.response.edit_message(embed=embed, view=view, ephemeral=True)
            
        button = discord.ui.Button(label="EXIT", style=discord.ButtonStyle.danger)
        button.callback = finishUpdate
        view.add_item(button)
        
        embed = createEditAttrEmbed(points)
        await interaction.response.edit_message(embed=embed, view=view, ephemeral=True)
    
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