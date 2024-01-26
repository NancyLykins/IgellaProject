import discord, os, requests
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")

async def createAbilitysEmbed(id):
    embed = discord.Embed(
    title="Habilidades"
    )
    try:
        response = requests.get(f"{url}/characters/{id}/abilitys")
        abilitys = response.json()
        for ability in abilitys:
            embed.add_field(name=ability[0].upper(), value=ability[1].capitalize(), inline=False)
    except:
        pass
    return embed