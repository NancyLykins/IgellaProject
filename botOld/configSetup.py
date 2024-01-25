import discord
from Commands.sql.classes.select.takeClassesName import takeClassesName
from Commands.sql.races.select.takeRacesName import takeRacesName
from Commands.sql.skills.select.takeSkillsName import takeSkillsName

async def configSetup(interaction):
    await createCategorys(interaction)
    await createTextChannels(interaction)
     
async def createCategorys(interaction):
    await createCategory(interaction, "Bestiário")
    await createCategory(interaction, "Game Master")
    await createCategory(interaction, "Players")
    
  
async def createTextChannels(interaction):
    await createTextChannel(interaction, "spawner", categoryName="Game Master")
    await createTextChannel(interaction, "testes", categoryName="Game Master")
              
       
async def createCategory(interaction, categoryName):
    category = discord.utils.get(interaction.guild.categories, name=categoryName)
    
    if category is None:
        category = await interaction.guild.create_category_channel(name=categoryName)
        permissions = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False)
        }
        await category.edit(overwrites=permissions)
        print(f"category {categoryName} created")
        
async def createTextChannel(interaction, name, categoryName=None):
    textChannel = discord.utils.get(interaction.guild.text_channels, name=name)
    
    if textChannel is None:
        if categoryName is not None:
            category = discord.utils.get(interaction.guild.categories, name=categoryName)
            await interaction.guild.create_text_channel(name=name, category=category)
            print(f"Text channel {name} create in {category}")
        else:
            await interaction.guild.create_text_channel(name=name)
            print(f"Text channel {name} created")
            
    else:
        print(f"Text channel {name} already exist")