import discord
from Commands.newObject.createObjects.waitForMessage import waitForMessage
from Commands.newObject.createObjects.waitForInt import waitForInt
from Commands.newObject.createObjects.askEffectInfos.askEffectBuffs import askEffectBuffs

effectInfos={
    "name": "",
    "id": 0,
    "agiBuff": 0,
    "forBuff": 0,
    "intBuff": 0,
    "preBuff": 0,
    "vigBuff": 0,
    "life": "",
    "mana": ""
}

async def createNewEffect(ctx, client):
    global effectInfos
    await ctx.message.delete()
    name = await waitForMessage(ctx, client, "Qual o nome do efeito?")
    effectInfos["name"] = name.lower()
    role = discord.utils.get(ctx.guild.roles, name=name.title())
    if role is None:
        color = await waitForMessage(ctx, client, "Qual a cor do efeito em HEX?", 1800)
        if color.startswith('#'):
            color = color[1:]
        effectRole = await ctx.guild.create_role(name=name.title())  
        try:
            await effectRole.edit(color= int(color, 16))
            effectInfos["id"] = effectRole.id
            await createUses(ctx, client, effectInfos)
        except:
            await ctx.send(">>> A cor tem que ser um codigo HEX válido")        
    else:
        await ctx.send(">>> Esse efeito já existe")
    
async def createUses(ctx, client, effectInfos):
    types = ["Vida", "Mana", "Status", "Outros"]
    view = discord.ui.View(timeout=180)
    
    async def uses(interaction: discord.Interaction):
        customId = interaction.data["custom_id"]
        
        match customId:
            case "Vida":
                embed = discord.Embed(
                    title="Quanto de vida esse efeito recupera"
                )
                embed.add_field(name="Inteiro", value="Você pode definir uma quantidade fixa de vida para ele, para inso deve enviar um valor inteiro\nEx: 100", inline=False)
                embed.add_field(name="Dado", value="Você pode definir o resultado de um dado\nEx: 2d6", inline=False)
                embed.add_field(name="Valores negativos", value="Se invez de recuperar a vida você quiser que esse item remova a mesma pode digitar '-' antes\nEx: -100 ou -2d6")
                await interaction.response.edit_message(content=None, embed=embed, view=None)
                
                def check(message):
                    return message.author == ctx.author and message.channel == ctx.channel
                
                value = await client.wait_for("message", check=check, timeout=180)
                value = value.content
                try:
                    value = int(value)
                except:
                    pass
                
                
                if(isinstance(value, int) or "d" in value):
                    if "d" in value:
                        parts = value.split("d")
                        try:
                            for part in parts:
                                print(f"Essa é a parte: |{part}|")
                                if part is None or part == "":
                                    pass
                                else:
                                    partInt = int(part)
                        except:
                            await ctx.send(">>> O valor digitado não é válido")
                            return
                        effectInfos["life"] = value
                        await askEffectBuffs(ctx, client, effectInfos)
                    else:
                        effectInfos["life"] = value
                        await askEffectBuffs(ctx, client, effectInfos)
                    
                else:
                    await ctx.send(">>> O valor digitado não é válido")
                
            case "Mana":    
                embed = discord.Embed(
                    title="Quanto de mana esse efeito recupera"
                )
                embed.add_field(name="Inteiro", value="Você pode definir uma quantidade fixa de mana para ele, para inso deve enviar um valor inteiro\nEx: 100", inline=False)
                embed.add_field(name="Dado", value="Você pode definir o resultado de um dado\nEx: 2d6", inline=False)
                embed.add_field(name="Valores negativos", value="Se invez de recuperar a mana você quiser que esse item remova a mesma pode digitar '-' antes\nEx: -100 ou -2d6")
                await interaction.response.edit_message(content=None, embed=embed, view=None)
                
                def check(message):
                    return message.author == ctx.author and message.channel == ctx.channel
                
                value = await client.wait_for("message", check=check, timeout=180)
                value = value.content
                try:
                    value = int(value)
                except:
                    pass
                
                
                if(isinstance(value, int) or "d" in value):
                    if "d" in value:
                        parts = value.split("d")
                        try:
                            parts[0] = int(parts[0])
                            parts[1] = int(parts[1])
                        except:
                            await ctx.send(">>> O valor digitado não é válido")
                            return
                        effectInfos["mana"] = value
                        await askEffectBuffs(ctx, client, effectInfos)
                    else:
                        effectInfos["mana"] = value
                        await askEffectBuffs(ctx, client, effectInfos)
                    
                else:
                    await ctx.send(">>> O valor digitado não é válido")
                
            case "Status":
                await interaction.message.delete()
                await askEffectBuffs(ctx, client, effectInfos)
                
            case "Outros":
                await interaction.response.edit_message(content=">>> Por favor fale com @u.hearv para saber mais", view=None)
                
    for type in types:
        button = discord.ui.Button(label=type, style=discord.ButtonStyle.primary)
        button.custom_id = type
        button.callback = uses
        view.add_item(button)
        
    await ctx.send(">>> Qual tipo de efeito é", view=view)