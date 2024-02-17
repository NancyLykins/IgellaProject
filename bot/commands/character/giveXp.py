import aiohttp, os
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")
header = {'Content-type': 'application/json'}
async def giveXp(interaction, player, xp):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{url}/characters/{player.id}/{xp}") as response:
            pass
    await interaction.response.send_message(f"{xp} de xp foi dado para {player.name}", ephemeral=True)
