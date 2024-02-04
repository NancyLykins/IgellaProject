import requests
from commands.tests.dices import d20
from commands.tests.calcAdvantage import calcAdvantage

async def rollAttr(ctx, teste: str):
    id = ctx.author.id  
    advantage = calcAdvantage(response = requests.get(f"http://localhost:5050/characters/{id}/{teste}"))
    diceResult = d20()
    total = diceResult + advantage
    await ctx.message.reply(f"""` {total} ` <-- [{diceResult}] {f'{""if (advantage == 0)else f"+ {advantage}"}' if (advantage >= 0) else advantage}""")
    