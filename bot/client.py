import discord, os, dotenv, re
from discord.ext import commands
from commands.setCommands import setCommands

from commands.tests.rollDice import rollDice
from commands.character.createCharacter import createCharacter
dotenv.load_dotenv
TOKEN = os.getenv("BOT_TOKEN")
client = commands.Bot(command_prefix=".", intents=discord.Intents.all())
DICERE = r"\d*d\d+(?:[\/\*\-\+\s]*\d+|\s*[\/\*\-\+\s]*\d*d\d+)*"

async def setup_hook():
    for root, dirs, files in os.walk("cogs"):
        for file in files:
            if not root.endswith("__pycache__"):
                path = os.path.join(root, file)[:-3].replace("/", ".")
                print(f"Loading {path}")
                await client.load_extension(path)

@client.event
async def on_ready():
    print("Creating dinamic commands")
    await setCommands(client)
    print("Starting to load cogs")
    await setup_hook()
    print("All cogs was loaded")
    synced = await client.tree.sync()
    print(f"Synced {len(synced)} command(s)")
    print(f"Client was started like: {client.user}")

@client.event
async def on_message(message):
  
    if re.fullmatch(DICERE, message.content):
        await rollDice(message)
    else:
        await client.process_commands(message)

@client.command(name="create")
async def create(ctx):
    await createCharacter(ctx, client)

client.run(TOKEN)