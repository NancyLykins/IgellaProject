import discord, os, requests
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")
skillsRank = {"S": 0, "A": 1, "B": 2, "C": 3, "D": 4, "F": 5}

async def createSkillsEmbed(id):
    embed = discord.Embed(
        title="Minhas Pericias:",
        colour=459375
    )

    response = requests.get(f"{url}/characters/{id}/skills")
    skills = response.json()
    
    
    skills = sorted(skills, key=lambda skill: (skillsRank[skill['rank']], skill['pericia']))
    
    for skill in skills:
        embed.add_field(name="", value=f"**{skill['pericia'].title()}: {skill['rank']}**", inline=False)

    return embed
