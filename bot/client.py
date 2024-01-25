import discord, cleanCache, asyncio, youtube_dl, checkCharacter, math, os
from discord import app_commands
from discord.ext import commands
from key import TOKEN
from cogs.loadCogs import setup_hook
client = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@client.event
async def on_ready():
    await setup_hook(client)
    synced = await client.tree.sync()
    print(f"Syncd {len(synced)} command(s)")
    await cleanCache.cleanCache(client)
    print(f"Bot is already started like: {client.user}")
    
client.run(TOKEN)