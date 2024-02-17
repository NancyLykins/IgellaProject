import discord, os, aiohttp
from commands.monster.createMemberButtons import createMemberButtons
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")
header = {'Content-type': 'application/json'}
async def monsterDeadExecute(interaction, client, monster):
    monsterName = monster["name"]
    monsterLife = monster["hp"]
    xpPerPleyer = (monster["lvl"]*4)-5
    body={
        "tempHp": monsterLife
    }
    async with aiohttp.ClientSession() as session:
        await session.patch(f"{url}/monsters/{monsterName}", json=body, headers=header)
        
    monsterName = monsterName.title()
    deadMessage = f"{monsterName} foi derrotado"
    embed = discord.Embed(
        title=deadMessage,
        description=f"**Xp:** {xpPerPleyer}"
    )
    embed.set_footer(text="Quem deve receber xp?")


    view = discord.ui.View()
    async def giveXpForMonsterDeth(interaction: discord.Interaction):
        memberName = interaction.data["custom_id"]
        async with aiohttp.ClientSession() as session:
            member = discord.utils.get(interaction.guild.members, name=memberName)
            id = member.id
            async with session.post(f"{url}/characters/{id}/{xpPerPleyer}") as response:
                pass
            
        for button in view.children:
            if button.label == memberName:
                button.disabled = True

        await interaction.message.delete()        
        await interaction.channel.send(embed=embed, view=view)

    view = await createMemberButtons(interaction, client, giveXpForMonsterDeth)
    await interaction.channel.send(embed=embed, view=view) #MARCAÇÃO
