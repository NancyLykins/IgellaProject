import discord
from Commands.sql.character.select.takeCharacter import takeCharacter

async def infosEmbed(playerId):
    character = takeCharacter(playerId)
    character = character[0]
    nome = character[1]
    idade = character[2]
    genero = character[3]
    raca = character[4]
    magia = character[5]
    classe = character[6]
    level = character[7]
    xpAtual = character[8]
    xpNextLvl = level*10
    maxHP = character[10]
    hp = character[11]
    maxMp = character[12]
    mp = character[13]
    agilidade = character[14]
    agilidadeBuff = character[15]
    forca = character[16]
    forcaBuff = character[17]
    inteligencia = character[18]
    inteligenciaBuff = character[19]
    presenca = character[20]
    presencaBuff = character[21]
    vigor = character[22]
    vigorBuff = character[23]
    pontosRestantes = character[24]
    armo = character[25]

    xpBar = calculateEXP(xpAtual, xpNextLvl)

    embed = discord.Embed(
        title = f"Nome: {nome}",
        colour = 000000
    ) 

    embed.add_field(name="", value=f"**Idade:**  {idade}")
    embed.add_field(name="", value=f"**Gênero:**  {genero}")
    embed.add_field(name="", value=f"**Raça:**  {raca}")
    embed.add_field(name="", value=f"**LEVEL:**  {level}")
    embed.add_field(name="", value=f"**CLASSE:**  {classe}")
    embed.add_field(name="", value=f"**MAGIA:**  {magia}")
    embed.add_field(name="", value=f"EXP: |{xpBar}|", inline=False)
    embed.add_field(name="", value="───────────────────────────────────────", inline=False)
    embed.add_field(name="", value=f"**HP:** {hp}/{maxHP}")
    embed.add_field(name="", value=f"**Armadura:** {armo}")
    embed.add_field(name="", value=f"**MP:** {mp}/{maxMp}", inline=False)
    embed.add_field(name="", value="───────────────────────────────────────", inline=False)
    embed.add_field(name="", value=f"""**AGILIDADE:**  {agilidade} {f'{""if (agilidadeBuff == 0)else f"+ {agilidadeBuff}"}' if (agilidadeBuff >= 0) else agilidadeBuff}""", inline=False)
    embed.add_field(name="", value=f"""**FORÇA:**  {forca} {f'{"" if (forcaBuff == 0)else f"+ {forcaBuff}"}' if (forcaBuff >= 0) else forcaBuff}""", inline=False)
    embed.add_field(name="", value=f"""**INTELIGENCIA:**  {inteligencia} {f'{"" if (inteligenciaBuff == 0)else f"+ {inteligenciaBuff}"}' if (inteligenciaBuff >= 0) else inteligenciaBuff}""", inline=False)
    embed.add_field(name="", value=f"""**PRESENÇA:**  {presenca} {f'{"" if (presencaBuff == 0)else f"+ {presencaBuff}"}' if (presencaBuff >= 0) else presencaBuff}""", inline=False)
    embed.add_field(name="", value=f"""**VIGOR:**  {vigor} {f'{"" if (vigorBuff == 0)else f"+ {vigorBuff}"}' if (vigorBuff >= 0) else vigorBuff}""", inline=False)
    
    embed.add_field(name="", value="───────────────────────────────────────", inline=False)  
    embed.set_footer(text=f"Pontos para distribuir: {pontosRestantes}")

    return embed


def calculateEXP(xpMin, xpMax):
    xpBar = ""
    currentXp = int(24*(xpMin/xpMax))
    remindXp = 24 - currentXp

    xpBar += "█"*currentXp #ALT 219
    xpBar += "░"*remindXp #ALT 176

    return xpBar
