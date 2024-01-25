from Commands.newObject.createObjects.waitForMessage import waitForMessage
from Commands.newObject.createObjects.askClassInfos.askClassBuffs import askClassBuffs

classInfos={
    "className": "",
    "classDescription": "",
    "agiBuff": 0,
    "forBuff": 0,
    "intBuff": 0,
    "preBuff": 0,
    "vigBuff": 0,
    "perBuff": 0
}

async def createNewClass(ctx, client):
    global classInfos
    await ctx.message.delete()
    classInfos["className"] = await waitForMessage(ctx, client, "Qual o nome da nova classe?")
    classInfos["classDescription"] = await waitForMessage(ctx, client, "Qual a descrição da classe?", 10800)
    await askClassBuffs(ctx, client, classInfos)