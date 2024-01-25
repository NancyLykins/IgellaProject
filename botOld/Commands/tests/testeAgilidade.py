import discord
from Commands.sql.tests.takeAttr import takeAttr
from Commands.tests.dices import d20
from Commands.tests.calcAdvantage import calcAdvantage

async def testeAgilidade(ctx):
    userId = ctx.author.id
    attr = ["agilidade", "agilidadeBuff"]
    
    agilidade, agilidadeBuff = await takeAttr(userId, attr)
    agilidade = agilidade + agilidadeBuff
    advantage = calcAdvantage(agilidade)
    diceResult = d20()
    total = diceResult + advantage
    await ctx.message.reply(f"""` {total} ` <-- [{diceResult}] {f'{""if (advantage == 0)else f"+ {advantage}"}' if (advantage >= 0) else advantage}""")
    