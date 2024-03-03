import requests, os
from dotenv import load_dotenv
from commands.tests.calcAdvantage import calcAdvantage
from commands.tests.dices import d20
from commands.tests.calculateSkillUses import calculateSkillUses

load_dotenv()
url = os.getenv("API_URL")

async def rollSkill(ctx, skill):
    difficultoToUp = 17
    skill = skill.lower()
    id = ctx.author.id
    buff = ctx.message.content.split(skill)[1]
    response = requests.get(f"{url}/characters/{id}/skills/{skill}")
    data = response.json()
    if data != []:
        data = data[0]
        skillBuff = data["buff"]
        attr = data["attr"]
    
    else:
        skillBuff = -1
        response = requests.get(f"{url}/skills/{skill}")
        attr = response.json()[0]["attr"]
        if attr == False:
            await ctx.send("Essa pericia não existe")
            return False
    
    match attr:
        case "AGI":
            atributes ="agilidade"
        case "FOR":
            atributes ="forca"
        case "INT":
            atributes ="inteligencia"
        case "PRE":
            atributes ="presenca"
        case "VIG":
            atributes = "vigor"
    
    response = requests.get(f"{url}/characters/{id}/{atributes}")
    advantage = calcAdvantage(int(response.json()))
    diceResult = d20()

    total = diceResult + advantage + skillBuff 
    if buff != "":
        buff = int(eval(buff))
        total += buff

    await ctx.message.reply(
        f"` {total} ` <-- [{diceResult}] "
        f"{'+ ' + str(advantage) if advantage > 0 else '' if advantage == 0 else ' - ' + str(-advantage)} "
        f"{'+ ' + str(skillBuff) if skillBuff > 0 else '' if skillBuff == 0 else ' ' + str(skillBuff)}"
        f"{' ' if (buff == '') else '+ ' + str(buff) if (buff > 0) else str(buff)}"
    )
    if(diceResult >= difficultoToUp):
        await calculateSkillUses(ctx, skill)