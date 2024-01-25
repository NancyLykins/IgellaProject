import discord
from Commands.sql.effects.saveEffect import saveEffect

attrList={
    "AGI": 0,
    "FOR": 0,
    "INT": 0,
    "PRE": 0,
    "VIG": 0,
}

attrKeys = list(attrList.keys())


async def askEffectBuffs(ctx, client, effectInfo):
    global attrList
    attrList["AGI"] = 0
    attrList["FOR"] = 0
    attrList["INT"] = 0
    attrList["PRE"] = 0
    attrList["VIG"] = 0

    view = discord.ui.View()
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
    
    async def saveEffectInfo(interaction: discord.Integration):
        await interaction.message.delete()
        effectInfo["agiBuff"] = attrList["AGI"]
        effectInfo["forBuff"] = attrList["FOR"]
        effectInfo["intBuff"] = attrList["INT"]
        effectInfo["preBuff"] = attrList["PRE"]
        effectInfo["vigBuff"] = attrList["VIG"]
        saveEffect(effectInfo)
        
        
        
    button = discord.ui.Button(label="EXIT", style=discord.ButtonStyle.red)
    button.callback = saveEffectInfo
    view.add_item(button)
    
    embed = createClassBuffEmbed()
    await ctx.send(embed=embed, view=view)

def createClassBuffEmbed():
    embed = discord.Embed(
        title="Atributos",
        description="Selecione os atributos que recebem bonus",
        colour= 325476
    )
    for attr in attrKeys:
        embed.add_field(name=attr, value=f" ` {attrList[attr]} `", inline=False)
        
    return embed

