import discord, os, dotenv
from discord.ext import commands
from commands.setCommands import setCommands
from commands.tests.attributes import rollAttr
from commands.tests.rollDice import rollDice
from commands.tests.rollSkill import rollSkill
from commands.character.createCharacter import createCharacter
dotenv.load_dotenv
TOKEN = os.getenv("BOT_TOKEN")

client = commands.Bot(command_prefix=".", intents=discord.Intents.all())

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
    await setCommands()
    print("Starting to load cogs")
    await setup_hook()
    print("All cogs was loaded")
    synced = await client.tree.sync()
    print(f"Synced {len(synced)} command(s)")
    print(f"Client was started like: {client.user}")

@client.command(name="create")
async def create(ctx):
    await createCharacter(ctx, client)


#   #############
#   #   TESTS   #
#   #############

@client.command()
async def roll(ctx):
    await rollDice(ctx)

@client.command()
async def usar(ctx, skill=None):
    if skill is not None:
        await rollSkill(ctx, skill)
    else:
        await ctx.send("Escolha uma perícia e tente novamente")
        
@client.command(name="agi")
async def AGI(ctx):
    try:
        await rollAttr(ctx, "agilidade")
    except:
        print("error")

@client.command(name="for")
async def FOR(ctx):
    try:
        await rollAttr(ctx, "forca")
    except:
        pass

@client.command(name="int")
async def INT(ctx):
    try:
        await rollAttr(ctx, "inteligencia")
    except:
        pass

@client.command(name="pre")
async def PRE(ctx):
    try:
        await rollAttr(ctx, "presenca")
    except:
        pass

@client.command(name="vig")
async def VIG(ctx):
    try:
        await rollAttr(ctx, "vigor")
    except:
        pass

client.run(TOKEN)