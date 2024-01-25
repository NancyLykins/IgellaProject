import os, discord
async def cleanCache(client):
    try:
        cachePath = "Cache"
        if os.listdir(cachePath) != []:
            for file in os.listdir(cachePath):
                os.remove(os.path.join(cachePath, file))
            print("Cache limpo")
        myGuild = discord.utils.get(client.guilds, id=1187645343173714021)
        testChannel = discord.utils.get(myGuild.text_channels, name="testes")
        await testChannel.purge()
    except:
        os.mkdir("Cache")