import discord, os ,aiohttp
from dotenv import load_dotenv
from commands.character.startCreation import Character
load_dotenv()
url = os.getenv("API_URL")
characters = {}
thisInteraction = {}
async def createCharacter(ctx, client: discord.Client):
    global characters, thisInteraction
    id = ctx.author.id
    thisInteraction[id] = None
    await ctx.message.delete()
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}/characters/{id}") as response:
            trigget = response.status
    if trigget == 404:      
        if thisInteraction[id] == 1:
            await ctx.send("Você já está em uma interação")
            return 0
        thisInteraction[id] = 1
        characters[id] = Character(ctx, client, id)
        await characters[id].ask_name()
        await characters[id].ask_gender()
        await characters[id].ask_age()
        await characters[id].set_power()
        await characters[id].ask_race()
        await characters[id].ask_attributes()
        await characters[id].ask_class()
        await characters[id].ask_skills()
        await characters[id].save()
        thisInteraction.pop(id)
    else:
        await ctx.send("Você já tem um personagem criado")
