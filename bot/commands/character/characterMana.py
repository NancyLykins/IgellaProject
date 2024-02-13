import discord, os, aiohttp
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")
header = {'Content-type': 'application/json'}

async def characterMana(interaction, player: discord.Member, mana: int, option):
    body = {"mp": f"{option}{mana}"}
    async with aiohttp.ClientSession() as session:
        await session.patch(f"{url}/characters/{interaction.user.id}", headers=header, json=body)  