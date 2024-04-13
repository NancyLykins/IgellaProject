import requests, os
from dotenv import load_dotenv
from commands.tests.dices import d20
from commands.tests.calcAdvantage import calcAdvantage

load_dotenv()
url = os.getenv("API_URL")

async def rollAttr(ctx, teste: str):
    id = ctx.author.id
    response = requests.get(f"{url}/characters/{id}/{teste}")
    advantage = calcAdvantage(response.json())
    diceResult = d20()
    total = diceResult + advantage
    await ctx.message.reply(f"""` {total} ` <-- [{diceResult}] {f'{""if (advantage == 0)else f"+ {advantage}"}' if (advantage >= 0) else advantage}""")
    