import discord
from Commands.sql.itens.saveItem import saveItem

attrList={"AGI": 0, "FOR": 0, "INT": 0, "PRE": 0, "VIG": 0}
realBuff = ""
trigget = 0

async def askItemBuff(interaction, client, itemInfos):
    global trigget
    if trigget  == 0:
        trigget += 1
        await interaction.channel.send(content=">>> O que esse equipamento oferece?", view=createView(client, itemInfos))
    else:
        await interaction.message.delete()
        await interaction.channel.send(content=">>> O que esse equipamento oferece?", view=createView(client, itemInfos))

def createView(client, itemInfos):
    type = {
        "armo": ["Armadura", discord.ButtonStyle.primary],
        "buff": ["Atributo", discord.ButtonStyle.primary],
        "effect": ["Efeito", discord.ButtonStyle.primary],
        "life": ["Vida", discord.ButtonStyle.primary],
        "save": ["Save", discord.ButtonStyle.green],
    }

    view = discord.ui.View()
    async def setBonus(interaction: discord.Interaction):
        customId = interaction.data["custom_id"]
        match customId:
            case "armo":
                await askArmo(interaction, client, itemInfos)
            case "buff":
                await askBuff(interaction, client, itemInfos)
            case "effect":
                await askEffect(interaction, client, itemInfos)
            case "life":
                await askLife(interaction, client, itemInfos)
            case "save":
                await save(interaction, itemInfos)


    for bonus in list(type.keys()):
        button = discord.ui.Button(label=type[bonus][0], style=type[bonus][1])
        button.custom_id = bonus
        button.callback = setBonus
        view.add_item(button)
    
    return view

################
#   ASK BUFF   #
################

attrBonus = {
    "agiBuff": 0,
    "forBuff": 0,
    "intBuff": 0,
    "preBuff": 0,
    "vigBuff": 0
}
async def askBuff(interaction, client, itemInfos ):
######################################## vvv BUTTON FUNCTIONS vvv ########################################  

    async def giveAttrBonus(interaction: discord.Integration):
        attr = interaction.data["custom_id"]
        attrList[attr] += 1
        await interaction.response.edit_message(embed=createRaceBuffEmbed())
   
    async def back(interaction: discord.Interaction):
        global attrBonus
        attrBonus["agilidadeBuff"] += attrList["AGI"]
        attrBonus["forcaBuff"] += attrList["FOR"]
        attrBonus["inteligenciaBuff"] += attrList["INT"]
        attrBonus["presencaBuff"] += attrList["PRE"]
        attrBonus["vigorBuff"] += attrList["VIG"]
        await saveAttr(itemInfos)
        await askItemBuff(interaction, client, itemInfos)

    async def saveItemInfos(interaction: discord.Integration):
        global attrBonus
        attrBonus["agilidadeBuff"] += attrList["AGI"]
        attrBonus["forcaBuff"] += attrList["FOR"]
        attrBonus["inteligenciaBuff"] += attrList["INT"]
        attrBonus["presencaBuff"] += attrList["PRE"]
        attrBonus["vigorBuff"] += attrList["VIG"]
        await saveAttr(itemInfos)
        await save(interaction, itemInfos)

######################################## ^^^ BUTTON FUNCTIONS ^^^ ########################################  
    view = discord.ui.View(timeout=180)
    ### VVV BACK BUTTON VVV ####
    button = discord.ui.Button(label="Voltar", style=discord.ButtonStyle.green)
    button.callback = back
    view.add_item(button)
  
    ### VVV ATTR BUTTON VVV ####
    for attr in list(attrList.keys()):
        button = discord.ui.Button(label=attr, style=discord.ButtonStyle.blurple)
        button.custom_id = attr
        button.callback = giveAttrBonus
        view.add_item(button)

    ### VVV EXIT BUTTON VVV ####
    button = discord.ui.Button(label="EXIT", style=discord.ButtonStyle.red)
    button.callback = saveItemInfos
    view.add_item(button)
    embed = createRaceBuffEmbed()
    await interaction.response.edit_message(embed=embed, view=view)

def createRaceBuffEmbed():
        global attrList
        embed = discord.Embed(
            title="Atributos",
            description="Selecione os atributos que recebem bonus",
            colour= 325476
        )
        for attr in list(attrList.keys()):
            embed.add_field(name=attr, value=f" ` {attrList[attr]} `", inline=False)
            
        return embed

async def saveAttr(itemInfos):
    global attrBonus, realBuff
    for buff in list(attrBonus.keys()):
        if(attrBonus[buff] != 0):
            realBuff += f"-{buff}:{attrBonus[buff]}"

    itemInfos["action"] += realBuff 


################
#   ASK ARMO   #
################

async def askArmo(interaction, client, itemInfos):
    def check(message):
        try:
            messageValue = int(message.content)
        except:
            pass   
        return message.author == interaction.user and interaction.channel == message.channel and isinstance(messageValue, int)

    view = discord.ui.View()
######################################## vvv BUTTON FUNCTIONS vvv ########################################  
    async def back(interaction: discord.Interaction):
        await askItemBuff(interaction, client, itemInfos) 
   
    async def exit(interaction: discord.Interaction):
        await save(interaction, itemInfos)
######################################## ^^^ BUTTON FUNCTIONS ^^^ ########################################  
    button = discord.ui.Button(label="Voltar", style=discord.ButtonStyle.red)
    button.callback = back
    view.add_item(button)
    
    button = discord.ui.Button(label="Save", style=discord.ButtonStyle.green)
    button.callback = exit
    view.add_item(button)
    
    
    await interaction.response.edit_message(content=">>> Quanto de defesa esse item da?", view=view, embed=None)
    response = await client.wait_for("message", check=check, timeout=180)
    await response.delete()
    armo = response.content
    itemInfos["action"] += f"-armo:{armo}"
    await askItemBuff(interaction, client, itemInfos)

    
##################
#   ASK EFFECT   #
##################

async def askEffect(interaction, client, itemInfos):
    def check(message):
        return message.author == interaction.user and message.channel == interaction.channel and message.content.startswith("<@&")
    
    view = discord.ui.View()
######################################## vvv BUTTON FUNCTIONS vvv ########################################  
    async def back(interaction: discord.Interaction):
        await askItemBuff(interaction, client, itemInfos) 
   
    async def exit(interaction: discord.Interaction):
        await save(interaction, itemInfos)
######################################## ^^^ BUTTON FUNCTIONS ^^^ ########################################  
    button = discord.ui.Button(label="Voltar", style=discord.ButtonStyle.red)
    button.callback = back
    view.add_item(button)
    
    button = discord.ui.Button(label="Save", style=discord.ButtonStyle.green)
    button.callback = exit
    view.add_item(button)
    
    
    await interaction.response.edit_message(content=">>> Qual efeito esse item da?", view=view, embed=None)
    effect = await client.wait_for("message", check=check)
    await effect.delete()
    itemInfos["action"] += f"-effect:{effect.content}"
    await askItemBuff(interaction, client, itemInfos)

async def save(interaction, itemInfos):
    global trigget
    trigget = 0
    await interaction.message.delete()
    await interaction.channel.send(">>> Item salvo com sucesso!!")
    saveItem(itemInfos)
      
################
#   ASK LIFE   #
################  
    
async def askLife(interaction, client, itemInfos):
    def check(message):
        try:
            messageValue = int(message.content)
        except:
            pass   
        return message.author == interaction.user and interaction.channel == message.channel and isinstance(messageValue, int)

    view = discord.ui.View()
######################################## vvv BUTTON FUNCTIONS vvv ########################################  
    async def back(interaction: discord.Interaction):
        await askItemBuff(interaction, client, itemInfos) 
   
    async def exit(interaction: discord.Interaction):
        await save(interaction, itemInfos)
######################################## ^^^ BUTTON FUNCTIONS ^^^ ########################################  
    button = discord.ui.Button(label="Voltar", style=discord.ButtonStyle.red)
    button.callback = back
    view.add_item(button)
    
    button = discord.ui.Button(label="Save", style=discord.ButtonStyle.green)
    button.callback = exit
    view.add_item(button)
    
    
    await interaction.response.edit_message(content=">>> Quanto de vida esse item da?", view=view, embed=None)
    response = await client.wait_for("message", check=check, timeout=180)
    await response.delete()
    life = response.content
    itemInfos["action"] += f"-maxHp:{life}"
    await askItemBuff(interaction, client, itemInfos)
