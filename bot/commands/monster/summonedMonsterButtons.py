import discord, os, aiohttp, asyncio
from commands.tests.rollNoPlayer import rollNoPlayer
from commands.monster.monsterDeadExecute import monsterDeadExecute
from commands.monster.summonedMonsterEmbed import summonedMonsterEmbed
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")
header = {'Content-type': 'application/json'}

class summonedMonsterButtons(discord.ui.View):
    def __init__(self, interaction: discord.Interaction, client: discord.Client, monster: dict):
        super().__init__(timeout=10800)
        self.value = None
        self.interaction = interaction
        self.client = client
        self.monster = monster
        self.name = monster["name"]
        self.mhp = monster["hp"]
        self.hp = monster["tempHp"]
        self.agi = monster["agilidade"]
        self.forca = monster["forca"]
        self.int = monster["inteligencia"]
        self.pre = monster["presenca"]
        self.vig = monster["vigor"]
       
    @discord.ui.button(label="AGI", style=discord.ButtonStyle.primary)
    async def rollAGI(self, interaction, button):
        await rollNoPlayer(interaction, self.agi)
        
    @discord.ui.button(label="FOR", style=discord.ButtonStyle.primary)
    async def rollFOR(self, interaction, button):
        await rollNoPlayer(interaction, self.forca)
        
    @discord.ui.button(label="INT", style=discord.ButtonStyle.primary)
    async def rollINT(self, interaction, button):
        await rollNoPlayer(interaction, self.int)
        
    @discord.ui.button(label="PRE", style=discord.ButtonStyle.primary)
    async def rollPRE(self, interaction, button):
        await rollNoPlayer(interaction, self.pre)
        
    @discord.ui.button(label="VIG", style=discord.ButtonStyle.primary)
    async def rollVIG(self, interaction, button):
        await rollNoPlayer(interaction, self.vig)
    
    @discord.ui.button(label="DAMAGE", style=discord.ButtonStyle.danger)
    async def takeDamage(self, interaction, button):
        monsterName = self.name
        client = self.client
        tempHp = self.hp
        
        await interaction.response.send_message(f">>> Quanto de dano o(a) {monsterName} levou?")

        def check(message):
            return message.author == interaction.user and message.channel == interaction.channel

        damage = await client.wait_for("message", check=check, timeout=120)
        await interaction.delete_original_response()
        await damage.delete()
        damage = int(damage.content)
        newLife = (tempHp - damage)
        
        if (newLife <= 0):
            await interaction.message.delete()
            await monsterDeadExecute(interaction, client, self.monster)
        
        else:
            body={
                "tempHp": f"-{damage}"
            }
            async with aiohttp.ClientSession() as session:
                await session.patch(f"{url}/monsters/{monsterName}", json=body, headers=header)
            embed, monster = await summonedMonsterEmbed(monsterName)
            await interaction.message.delete()
            await interaction.channel.send(embed=embed, view=self)
              
    @discord.ui.button(label="KILL", style=discord.ButtonStyle.danger)
    async def killMonster(self, interaction, button):
        client = self.client
        await interaction.message.delete()
        await monsterDeadExecute(interaction, client, self.monster)