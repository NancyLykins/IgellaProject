import discord
from Commands.sql.monsters.select.takeMonster import takeMonster


async def summonedMonsterEmbed(monsterName):
    monster = takeMonster(monsterName)
    name = monster[0]
    img = monster[1]
    lvl = monster[2]
    hp = monster[3]
    tempHp = monster[4]
    agi = monster[5]
    forca = monster[6]
    int = monster[7]
    pre = monster[8]
    vig = monster[9]
    
    embed = discord.Embed(
        title = name.title(),
        description=f"Level: {lvl}",
        colour= 328943
    )
    embed.add_field(name="", value=f"**HP:**  {tempHp}/{hp}", inline=False)
    embed.add_field(name="** **AGI", value=f"` {agi} `")
    embed.add_field(name="** **FOR", value=f"` {forca} `")
    embed.add_field(name="** **INT", value=f"` {int} `")
    embed.add_field(name="** **PRE", value=f"` {pre} `")
    embed.add_field(name="** **VIG", value=f"` {vig} `")
    embed.add_field(name="** **", value="** **")
    embed.set_image(url=img)
    
    return embed, monster