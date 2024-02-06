import discord, requests, os
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")

async def createEquipsEmbed(id):
    slots = {
        "head":['_vazio_', ''],
        "chest":['_vazio_', ''],
        "legs":['_vazio_', ''],
        "feets":['_vazio_', '']
    }
    embed = discord.Embed(
        title = "Equipamentos",
        colour = 151515
    )
    response = requests.get(f"{url}/characters/{id}/equips")
    equips = response.json()
    for item in equips:
        if(item["head"] is not None and item["head"] == item["rowId"]):
            slots["head"][0] = item["name"]
            slots["head"][1] = item["emoji"]
        elif(item["chest"] is not None and item["chest"] == item["rowId"]):
            slots["chest"][0] = item["name"]
            slots["chest"][1] = item["emoji"]
        elif(item["legs"] is not None and item["legs"] == item["rowId"]):
            slots["legs"][0] = item["name"]
            slots["legs"][1] = item["emoji"]
        elif(item["feets"] is not None and item["feets"] == item["rowId"]):
            slots["feets"][0] = item["name"]
            slots["feets"][1] = item["emoji"]
            
    embed.add_field(name="------------------", value="", inline=False)
    embed.add_field(name=f"Cabeça {slots['head'][1]}", value=(slots['head'][0]), inline=False)
    embed.add_field(name=f"Peito {slots['chest'][1]}", value=(slots['chest'][0]), inline=False)
    embed.add_field(name=f"Calça {slots['legs'][1]}", value=(slots['legs'][0]), inline=False)
    embed.add_field(name=f"Bota {slots['feets'][1]}", value=(slots['feets'][0]), inline=False)

    return embed
