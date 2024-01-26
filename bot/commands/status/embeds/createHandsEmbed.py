import discord, requests, os
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")

async def createHandsEmbed(id):
    embed = discord.Embed(
        title= "Equipamentos",
        colour = 678295
    )
    response = requests.get(f"{url}/characters/{id}/hands")
    hands = response.json()
    itenEquiped = len(hands)
    if(itenEquiped > 0):
        rightH = hands[0]
        if(rightH["slot"] != "twoH"):
            try:
                leftH = hands[1]
            except:
                leftH = {
                    "name": '_vazio_',
                    "emoji": ''
                }
        else:
            leftH = {
                "name": '',
                "emoji": '🚫'
            }
    else:
        rightH = {
            "name": '_vazio_',
            "emoji": ''
        }
        leftH = {
            "name": '_vazio_',
            "emoji": ''
        }

    embed.add_field(name=f"Mão Direita {rightH['emoji']}", value=rightH['name'].title())
    embed.add_field(name=f"Mão Esquerda {leftH['emoji']}", value=leftH['name'].title())

    return embed
