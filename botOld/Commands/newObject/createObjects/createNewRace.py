from Commands.newObject.createObjects.waitForMessage import waitForMessage
from Commands.newObject.createObjects.askRaceInfos.askRaceEmoji import askRaceEmoji
from Commands.newObject.createObjects.askRaceInfos.askRaceBuffs import askRaceBuffs

raceInfos={
    "raceName": "",
    "raceEmoji": "",
    "raceDescription": "",
    "agiBuff": 0,
    "forBuff": 0,
    "intBuff": 0,
    "preBuff": 0,
    "vigBuff": 0,
    "perBuff": 0
}

async def createNewRace(ctx, client):
    global raceInfos
    await ctx.message.delete()
    raceInfos["raceName"] = await waitForMessage(ctx, client, "Qual o nome da nova raça?")
    raceInfos["raceEmoji"] = await askRaceEmoji(ctx, client)
    raceInfos["raceDescription"] = await waitForMessage(ctx, client, "Qual a descrição da raça?", 10800)
    await askRaceBuffs(ctx, client, raceInfos)