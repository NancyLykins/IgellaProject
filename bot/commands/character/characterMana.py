import discord, os, aiohttp
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")
header = {'Content-type': 'application/json'}

async def characterMana(interaction, player: discord.Member, mana: int, option):
    body = {"mp": f"{option}{mana}"}
    async with aiohttp.ClientSession() as session:
        async with session.patch(f"{url}/characters/{player.id}", headers=header, json=body) as response:
            await interaction.response.send_message(f"{mana} {'foram' if mana > 1 else 'foi'} {'removida' if option == '-' else 'restaurada'} de {player}")