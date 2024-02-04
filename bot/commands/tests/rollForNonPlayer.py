from commands.tests.calcAdvantage import calcAdvantage
from commands.tests.dices import d20

async def rollForNonPlayer(interaction, attr):
    advantage = calcAdvantage(attr)
    diceResult = d20()
    sum = diceResult + advantage
    await interaction.response.send_message(f"""` {sum} ` <-- [{diceResult}] {f'{""if (advantage == 0)else f"+ {advantage}"}' if (advantage >= 0) else advantage}""")
