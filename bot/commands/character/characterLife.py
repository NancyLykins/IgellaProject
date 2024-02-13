import discord, os, aiohttp
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")
header = {'Content-type': 'application/json'}

async def characterLife(interaction, player: discord.Member, life: int, option):
    body = {"hp": f"{option}{life}"}
    async with aiohttp.ClientSession() as session:
        await session.patch(f"{url}/characters/{interaction.user.id}", headers=header, json=body)  