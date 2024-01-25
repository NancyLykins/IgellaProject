import discord
from Commands.sql.character.select.takeAbility import takeAbility

async def abilityEmbed(id):
    embed = discord.Embed(
        title="Habilidades"
    )
    try:
        for ability in takeAbility(id):
            embed.add_field(name=ability[0].upper(), value=ability[1].capitalize(), inline=False)
    except:
        pass
    return embed