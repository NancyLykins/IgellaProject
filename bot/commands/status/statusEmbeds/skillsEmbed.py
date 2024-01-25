import discord
from Commands.sql.character.select.takeSkills import takeSkills

async def skillsEmbed(id):
    embed = discord.Embed(
        title="Minhas Pericias:",
        colour=459375
    )

    pericias = takeSkills(id)

    skillsRank = {"S": 0, "A": 1, "B": 2, "C": 3, "D": 4, "F":5}
    
    pericias = sorted(pericias, key=lambda skill: (skillsRank[skill[2]], skill[1]))
    
    for pericia in pericias:
        embed.add_field(name="", value=f"**{pericia[1].title()}: {pericia[2]}**", inline=False)

    return embed
