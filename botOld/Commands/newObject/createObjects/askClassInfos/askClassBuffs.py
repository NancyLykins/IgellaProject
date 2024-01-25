import discord
from Commands.sql.classes.saveClass import saveClass

attrList={
    "AGI": 0,
    "FOR": 0,
    "INT": 0,
    "PRE": 0,
    "VIG": 0,
    "MAESTRIA": 0
}

attrKeys = list(attrList.keys())

class questionButtons(discord.ui.View):
    def __init__(self, classInfos, ctx):
        super().__init__()
        self.value = None
        self.classInfos = classInfos
        self.ctx = ctx
    
    @discord.ui.button(label="SIM", style=discord.ButtonStyle.green)
    async def yesButtonPress(self, interaction, button):
        await interaction.message.delete()
        view = discord.ui.View()
        ctx = self.ctx
        async def sumAttr(interaction: discord.Integration):
            global attrList
            attr = interaction.data["custom_id"]
            attrList[attr] += 1
            embed = createClassBuffEmbed()
            await interaction.response.edit_message(embed=embed)
        
        for attr in attrKeys:
            button = discord.ui.Button(label=attr, style=discord.ButtonStyle.blurple)
            button.custom_id = attr
            button.callback = sumAttr
            view.add_item(button)
        
        async def saveClassInfos(interaction: discord.Integration):
            classInfos = self.classInfos
            classInfos["agiBuff"] = attrList["AGI"]
            classInfos["forBuff"] = attrList["FOR"]
            classInfos["intBuff"] = attrList["INT"]
            classInfos["preBuff"] = attrList["PRE"]
            classInfos["vigBuff"] = attrList["VIG"]
            classInfos["perBuff"] = attrList["MAESTRIA"]
            await save(interaction, classInfos)
            
            
            
        button = discord.ui.Button(label="EXIT", style=discord.ButtonStyle.red)
        button.callback = saveClassInfos
        view.add_item(button)
        embed = createClassBuffEmbed()
        await ctx.send(embed=embed, view=view)
             
    
    @discord.ui.button(label="NÃO", style=discord.ButtonStyle.red)
    async def noButton(self, interaction, button):
        await save(interaction, self.classInfos)
  
async def askClassBuffs(ctx, client, classInfos):
    global attrList
    attrList["AGI"] = 0
    attrList["FOR"] = 0
    attrList["INT"] = 0
    attrList["PRE"] = 0
    attrList["VIG"] = 0
    attrList["MAESTRIA"] = 0
    await ctx.send(">>> Essa classe oferece algum buff??\nSe sim quais?", view=questionButtons(classInfos, ctx))

def createClassBuffEmbed():
    embed = discord.Embed(
        title="Atributos",
        description="Selecione os atributos que recebem bonus",
        colour= 325476
    )
    for attr in attrKeys:
        embed.add_field(name=attr, value=f" ` {attrList[attr]} `", inline=False)
        
    return embed

async def save(interaction, classInfos):
    await interaction.message.delete()
    saveClass(classInfos)
