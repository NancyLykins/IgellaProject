import discord, os
from discord.ext import commands
from key import TOKEN

CLIENT = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@CLIENT.event
async def on_ready():
    print("Starting to load cogs")
    for root, dirs, files in os.walk("cogs"):
        for file in files:
            if not root.endswith("__pycache__"):
                path = os.path.join(root, file)[:-3].replace("/", ".")
                print(f"Loading {path}")
                await CLIENT.load_extension(path)
    print("All cogs was loaded")
    synced = await CLIENT.tree.sync()
    print(f"Synced {len(synced)} command(s)")
    print(f"Client was started like: {CLIENT.user}")

CLIENT.run(TOKEN)