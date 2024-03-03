import discord
from commands.monster.summonedMonsterEmbed import summonedMonsterEmbed
from commands.monster.summonedMonsterButtons import summonedMonsterButtons

async def summonMonster(interaction: discord.Interaction, client: discord.Client, monsterName):
    monsterName = monsterName.lower()
    embed, monster = await summonedMonsterEmbed(monsterName)
    spawner = discord.utils.get(interaction.guild.text_channels, name="spawner")
    view = summonedMonsterButtons(interaction, client, monster)
    await spawner.send(embed=embed, view=view)
    await interaction.response.send_message(f">>> {monster['name'].title()} sumonado com sucesso em {spawner.mention}")