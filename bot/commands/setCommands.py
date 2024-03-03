import discord, aiohttp, os
from dotenv import load_dotenv
from discord.ext import commands
from commands.tests.attributes import rollAttr
from commands.tests.rollSkill import rollSkill
load_dotenv()
url = os.getenv("API_URL")

async def make_command(attr):
    async def command(ctx):
        await rollAttr(ctx, attr)
    return command

async def setCommands(client: discord.Client):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}/skills") as response:
            data = await response.json()
            print("Creating skills commands")
            for skill in data:
                await creteSkillCommands(client, skill["name"])
                print(f"Created: {skill['name']} command")
            print("All skill commands was created")
            
    commands = {
        "agi": make_command("agilidade"),
        "for": make_command("forca"),
        "pre": make_command("presenca"),
        "int": make_command("inteligencia"),
        "vig": make_command("vigor"),
    }
    print("Creating attributes commands")
    for nome, callBack in commands.items():
        client.command(name=nome)(await callBack)
        print(f"Created: {nome} command")
    print("All attributes commands was created")
        
async def creteSkillCommands(client, skill):
    async def makeCommand(skill):
        async def command(ctx):
            await rollSkill(ctx, skill)
        return command
    client.command(name=skill)(await makeCommand(skill))