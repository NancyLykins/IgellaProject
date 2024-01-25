import discord
from Commands.newObject.createObjects.waitForMessage import waitForMessage
from Commands.sql.skills.saveSkill import saveSkill

attrList = ["AGI", "FOR", "INT", "PRE", "VIG"]

async def createNewSkill(ctx, client):
    skillName = await waitForMessage(ctx, client, "Qual o nome da perícia?")
    skillDesc = await waitForMessage(ctx, client, "Qual a descrição da perícia?", 10800)
    
    view = discord.ui.View()
    
    async def chooseAttr(interaction: discord.Interaction):
        skillAttr = interaction.data["custom_id"]
        await interaction.message.delete()
        saveSkill(skillName, skillDesc, skillAttr)
    
    for attr in attrList:
        button = discord.ui.Button(label=attr, style=discord.ButtonStyle.primary)
        button.custom_id = attr
        button.callback = chooseAttr
        view.add_item(button)
    
    
    await ctx.send(">>> Qual atributo essa pericia usa?", view=view)