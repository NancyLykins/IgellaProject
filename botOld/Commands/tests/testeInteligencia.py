import discord
from Commands.sql.tests.takeAttr import takeAttr
from Commands.tests.dices import d20
from Commands.tests.calcAdvantage import calcAdvantage

async def testeInteligencia(ctx):
    userId = ctx.author.id
    attr = ["inteligencia", "inteligenciaBuff"]
    
    inteligencia, inteligenciaBuff = await takeAttr(userId, attr)
    inteligencia = inteligencia + inteligenciaBuff
    advantage = calcAdvantage(inteligencia)
    diceResult = d20()
    total = diceResult + advantage
    await ctx.message.reply(f"""` {total} ` <-- [{diceResult}] {f'{""if (advantage == 0)else f"+ {advantage}"}' if (advantage >= 0) else advantage}""")