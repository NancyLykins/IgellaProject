import discord
from Commands.sql.character.select.equip.takeHandsEquip import takeHandsEquip

async def handEquipamentEmbed(playerId):
    embed = discord.Embed(
        title= "Equipamentos",
        colour = 678295
    )
    result = takeHandsEquip(playerId)
    itenEquiped = len(result)
    if(itenEquiped > 0):
        rightH = result[0]
        if(rightH[2] != "twoH"):
            try:
                leftH = result[1]
            except:
                leftH = ['_vazio_','']
        else:
            leftH = ('','🚫')
    else:
        rightH = ['_vazio_','']
        leftH = ['_vazio_','']
        
        
    embed.add_field(name=f"Mão Direita {rightH[1]}", value=rightH[0].title())
    embed.add_field(name=f"Mão Esquerda {leftH[1]}", value=leftH[0].title())
    # embed.add_field(name="", value="", inline=False)
    # embed.add_field(name="Anel-1 [X]", value="[Equipado]")
    # embed.add_field(name="Anel-2 [X]", value="[Equipado]")

    return embed
