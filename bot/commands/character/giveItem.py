import discord, aiohttp, os
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")
header = {'Content-type': 'application/json'}
async def giveItem(interaction, player, item, amount):
    async with aiohttp.ClientSession() as session:
        body={
            item: amount
        }
        async with session.post(f"{url}/characters/{player.id}/inventary/{item}", json=body, headers=header) as response:
            if response.status == 404:
                await interaction.response.send_message("Nenhum item foi encontrado", ephemeral=True)           
            else:
                await interaction.response.send_message(f"{item} foi dado para {interaction.user.mention}")