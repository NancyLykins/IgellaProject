import discord
from Commands.sql.monsters.update.reduceMonsterLife import reduceMonsterLife
from Commands.monsters.createButtonForOnlineMembers import createButtonForOnlineMembers
from Commands.character.checkCharacterLevel import checkCharacterLevel

async def monsterDeadExecute(ctx, interaction, client, monster):
        monsterName = monster[0]
        monsterLife = monster[3]
        xpPerPleyer = (monster[2]*4)-5
        reduceMonsterLife(monsterName, monsterLife) 
         
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
            for member in ctx.guild.members:
                if member.name == memberName:
                    playerId = member.id
                
            await checkCharacterLevel(playerId, xpPerPleyer)    
                   
            for button in view.children:
                if button.label == memberName:
                    button.disabled = True
            
            await interaction.message.delete()        
            await interaction.channel.send(embed=embed, view=view)
            
        view = await createButtonForOnlineMembers(ctx, client, giveXpForMonsterDeth)
        await interaction.channel.send(embed=embed, view=view) #MARCAÇÃO
   