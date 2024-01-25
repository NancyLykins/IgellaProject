import discord
from Commands.sql.character.select.equip.takeBodyEquip import takeBodyEquip

async def bodyEquipamentEmbed(characterId):
    slots = {
        "head":['_vazio_', ''],
        "chest":['_vazio_', ''],
        "legs":['_vazio_', ''],
        "feets":['_vazio_', '']
    }
    embed = discord.Embed(
        title = "Equipamentos",
        colour = 151515
    )
    for item in takeBodyEquip(characterId):
        if item[2] is not None:
            slots[item[2]] = item
    embed.add_field(name="------------------", value="", inline=False)
    embed.add_field(name=f"Cabeça {slots['head'][1]}", value=(slots['head'][0]), inline=False)
    embed.add_field(name=f"Peito {slots['chest'][1]}", value=(slots['chest'][0]), inline=False)
    embed.add_field(name=f"Calça {slots['legs'][1]}", value=(slots['legs'][0]), inline=False)
    embed.add_field(name=f"Bota {slots['feets'][1]}", value=(slots['feets'][0]), inline=False)

    return embed
