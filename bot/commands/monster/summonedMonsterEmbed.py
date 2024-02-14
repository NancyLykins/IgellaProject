import discord, aiohttp, os
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")

async def summonedMonsterEmbed(monsterName):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}/monsters/{monsterName}") as response:
            data = (await response.json())[0]
    name = data["name"]
    img = data["img"]
    lvl = data["lvl"]
    hp = data["hp"]
    tempHp = data["tempHp"]
    agi = data["agilidade"]
    forca = data["forca"]
    int = data["inteligencia"]
    pre = data["presenca"]
    vig = data["vigor"]
    
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

    return embed, data