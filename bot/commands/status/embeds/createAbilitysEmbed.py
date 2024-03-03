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
            embed.add_field(name=ability["name"].upper(), value=ability["desc"].capitalize(), inline=False)
    except:
        pass
    return embed