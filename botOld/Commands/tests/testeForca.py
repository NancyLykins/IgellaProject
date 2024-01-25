import discord
from Commands.sql.tests.takeAttr import takeAttr
from Commands.tests.dices import d20
from Commands.tests.calcAdvantage import calcAdvantage

async def testeForca(ctx):
    userId = ctx.author.id
    attr = ["forca", "forcaBuff"]
    
    forca, forcaBuff = await takeAttr(userId, attr)
    forca = forca + forcaBuff
    advantage = calcAdvantage(forca)
    diceResult = d20()
    total = diceResult + advantage
    await ctx.message.reply(f"""` {total} ` <-- [{diceResult}] {f'{""if (advantage == 0)else f"+ {advantage}"}' if (advantage >= 0) else advantage}""")