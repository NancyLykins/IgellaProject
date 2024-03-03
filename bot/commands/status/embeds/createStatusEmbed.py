import discord, os, requests
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")

async def createStatusEmbed(id):
    response = requests.get(f"{url}/characters/{id}")
    character = response.json()[0]
    agilidadeBuff = character['agilidadeBuff']
    forcaBuff = character['forcaBuff']
    inteligenciaBuff = character['inteligenciaBuff']
    presencaBuff = character['presencaBuff']
    vigorBuff = character['vigorBuff']
    xpBar = calculateEXP(character['xpAtual'], character['xpNextLvl'])

    embed = discord.Embed(
        title = f"Nome: {character['nome']}",
        colour = 000000
    ) 

    embed.add_field(name="", value=f"**Idade:**  {character['idade']}")
    embed.add_field(name="", value=f"**Gênero:**  {character['genero']}")
    embed.add_field(name="", value=f"**Raça:**  {character['raca']}")
    embed.add_field(name="", value=f"**LEVEL:**  {character['level']}")
    embed.add_field(name="", value=f"**CLASSE:**  {character['classe']}")
    embed.add_field(name="", value=f"**MAGIA:**  {character['magia']}")
    embed.add_field(name="", value=f"EXP: |{xpBar}|", inline=False)
    embed.add_field(name="", value="───────────────────────────────────────", inline=False)
    embed.add_field(name="", value=f"**HP:** {character['hp']}/{character['maxHP']}")
    embed.add_field(name="", value=f"**Armadura:** {character['armo']}")
    embed.add_field(name="", value=f"**MP:** {character['mp']}/{character['maxMp']}", inline=False)
    embed.add_field(name="", value="───────────────────────────────────────", inline=False)
    embed.add_field(name="", value=f"""**AGILIDADE:**  {character['agilidade']} {f'{""if (agilidadeBuff == 0)else f"+ {agilidadeBuff}"}' if (agilidadeBuff >= 0) else agilidadeBuff}""", inline=False)
    embed.add_field(name="", value=f"""**FORÇA:**  {character['forca']} {f'{"" if (forcaBuff == 0)else f"+ {forcaBuff}"}' if (forcaBuff >= 0) else forcaBuff}""", inline=False)
    embed.add_field(name="", value=f"""**INTELIGENCIA:**  {character['inteligencia']} {f'{"" if (inteligenciaBuff == 0)else f"+ {inteligenciaBuff}"}' if (inteligenciaBuff >= 0) else inteligenciaBuff}""", inline=False)
    embed.add_field(name="", value=f"""**PRESENÇA:**  {character['presenca']} {f'{"" if (presencaBuff == 0)else f"+ {presencaBuff}"}' if (presencaBuff >= 0) else presencaBuff}""", inline=False)
    embed.add_field(name="", value=f"""**VIGOR:**  {character['vigor']} {f'{"" if (vigorBuff == 0)else f"+ {vigorBuff}"}' if (vigorBuff >= 0) else vigorBuff}""", inline=False)
    
    embed.add_field(name="", value="───────────────────────────────────────", inline=False)  
    embed.set_footer(text=f"Pontos para distribuir: {character['pontosRestantes']}")

    return embed


def calculateEXP(xpMin, xpMax):
    xpBar = ""
    currentXp = int(24*(xpMin/xpMax))
    remindXp = 24 - currentXp

    xpBar += "█"*currentXp #ALT 219
    xpBar += "░"*remindXp #ALT 176

    return xpBar