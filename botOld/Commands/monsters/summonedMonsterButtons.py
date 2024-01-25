from typing import Optional
import discord

from Commands.monsters.summonedMonsterEmbed import summonedMonsterEmbed
from Commands.sql.monsters.update.reduceMonsterLife import reduceMonsterLife
from Commands.sql.monsters.select.takeMonster import takeMonster
from Commands.monsters.monsterDeadExecute import monsterDeadExecute
from Commands.tests.rollForNonPlayer import rollForNonPlayer

class summonedMonsterButtons(discord.ui.View):
    def __init__(self, ctx, client, monster):
        super().__init__(timeout=10800)
        self.value = None
        self.ctx = ctx
        self.client = client
        self.monster = monster
        self.agi = monster[5]
        self.forca = monster[6]
        self.int = monster[7]
        self.pre = monster[8]
        self.vig = monster[9]
        
    @discord.ui.button(label="AGI", style=discord.ButtonStyle.primary)
    async def rollAGI(self, interaction, button):
        await rollForNonPlayer(interaction, self.agi)
        
    @discord.ui.button(label="FOR", style=discord.ButtonStyle.primary)
    async def rollFOR(self, interaction, button):
        await rollForNonPlayer(interaction, self.forca)
        
    @discord.ui.button(label="INT", style=discord.ButtonStyle.primary)
    async def rollINT(self, interaction, button):
        await rollForNonPlayer(interaction, self.int)
        
    @discord.ui.button(label="PRE", style=discord.ButtonStyle.primary)
    async def rollPRE(self, interaction, button):
        await rollForNonPlayer(interaction, self.pre)
        
    @discord.ui.button(label="VIG", style=discord.ButtonStyle.primary)
    async def rollVIG(self, interaction, button):
        await rollForNonPlayer(interaction, self.vig)
    
    @discord.ui.button(label="DAMAGE", style=discord.ButtonStyle.danger)
    async def takeDamage(self, interaction, button):
        monsterName = self.monster[0]
        ctx = self.ctx
        client = self.client
        monster = takeMonster(monsterName)
        tempHp = monster[4]
        try:
            await interaction.response.send_message()
        except:
            msg = await interaction.channel.send(f">>> Quanto de dano o(a) {monsterName} levou?")
            
        def check(message):
            return message.author == ctx.author and message.channel == interaction.channel
    
        damage = await client.wait_for("message", check=check, timeout=120)
        await msg.delete()
        await damage.delete()
        damage = int(damage.content)
        newLife = (tempHp - damage)
        if (newLife <= 0):
            await interaction.message.delete()
            await monsterDeadExecute(ctx, interaction, client, monster)
        else: 
            reduceMonsterLife(monsterName, newLife)
            embed, monster = await summonedMonsterEmbed(monsterName)
            await interaction.message.edit(embed=embed, view=self)
              
    @discord.ui.button(label="KILL", style=discord.ButtonStyle.danger)
    async def killMonster(self, interaction, button):
        client = self.client
        monster = list(self.monster)
        await interaction.message.delete()
        await monsterDeadExecute(self.ctx, interaction, client, monster)
        
           
     
        
