from Commands.sql.character.select.takeSkillBuffAndAttr import takeSkillBuffAndAttr
from Commands.sql.tests.takeAttr import takeAttr
from Commands.tests.calcAdvantage import calcAdvantage
from Commands.tests.dices import d20
from Commands.sql.skills.select.takeSkillAttr import takeSkillAttr
from Commands.rollSkill.calculateSkillUses import calculateSkillUses

async def rollSkill(ctx, skill):
    difficultoToUp = 20
    skill = skill.lower()
    playerId = ctx.author.id
    buff = ctx.message.content.split(skill)[1]
    result = takeSkillBuffAndAttr(playerId, skill)
    if result != "0":
        skillBuff, attr = result
    
    else:
        skillBuff = -1
        attr = takeSkillAttr(skill)
        if attr == False:
            await ctx.send("Essa pericia não existe")
            return False
    
    match attr:
        case "AGI":
            atributes = ["agilidade", "agilidadeBuff"]
        case "FOR":
            atributes = ["forca", "forcaBuff"]
        case "INT":
            atributes = ["inteligencia", "inteligenciaBuff"]
        case "PRE":
            atributes = ["presenca", "presencaBuff"]
        case "VIG":
            atributes = ["vigor", "vigorBuff"]
    
    attr, attrBuff = await takeAttr(playerId, atributes)
    attr = attr + attrBuff
    advantage = calcAdvantage(attr)
    diceResult = d20()

    total = diceResult + advantage + skillBuff 
    print(buff)
    if buff != "":
        buff = int(eval(buff))
        total += buff

    await ctx.message.reply(
        f"` {total} ` <-- [{diceResult}] "
        f"{'+ ' + str(advantage) if advantage > 0 else '' if advantage == 0 else ' - ' + str(-advantage)} "
        f"{'+ ' + str(skillBuff) if skillBuff > 0 else '' if skillBuff == 0 else ' ' + str(skillBuff)}"
        f"{' ' if (buff == '') else '+ ' + str(buff) if (buff > 0) else str(buff)}"
    )
    if(total >= difficultoToUp):
        await calculateSkillUses(ctx, skill)