import discord
from Commands.monsters.summonedMonsterEmbed import summonedMonsterEmbed
from Commands.monsters.summonedMonsterButtons import summonedMonsterButtons

async def summonMonster(ctx, client, monsterName):
    await ctx.message.delete()
    monsterName = monsterName.lower()
    embed, monster = await summonedMonsterEmbed(monsterName)
    
    spawner = discord.utils.get(ctx.guild.text_channels, name="spawner")
    view = summonedMonsterButtons(ctx, client, monster)
    await spawner.send(embed=embed, view=view)
        
        