import discord
from Commands.sql.monsters.delete.extinguishMonster import extinguishMonster

async def extingMonster(ctx, client, monsterName):
    monsterName = monsterName.lower()
    monsterPage = discord.utils.get(ctx.guild.text_channels, name=monsterName)
    await monsterPage.delete()
    extinguishMonster(monsterName)