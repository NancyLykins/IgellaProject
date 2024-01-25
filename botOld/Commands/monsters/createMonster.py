import discord, requests
from Commands.sql.monsters.Insert.saveMonster import saveMonster

monster = {
    "name": "",
    "img": "",
    "lvl": "",
    "hp": "",
    "tempHp": "",
    "agi": "",
    "for": "",
    "int": "",
    "pre": "",
    "vig": "",
}

async def createMonster(ctx, client):
    global monster
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    async def monsterName():
        try:
            await ctx.message.delete()
            msg = await ctx.send("Qual o nome/spécie da criatura?")    
            monsterName = await client.wait_for("message", check=check, timeout=120)
            newMonsterName = monsterName.content
            monster["name"] = newMonsterName.lower()
            
            await msg.delete()
            await monsterName.delete()

        except:
            await ctx.send("[Timeout] time: 2 minutes") 
    
    async def monsterImg():
        try:
            msg = await ctx.send("Qual a aparencia da criatura?")    
            monsterImg = await client.wait_for("message", check=check, timeout=120)
            attachment = monsterImg.attachments
            
            if(attachment):
                attachment = attachment[0]
                imgUrl = attachment.url
            else:
                imgUrl = monsterImg.content

            imgName = f"{monster['name']}.png" 
            response = requests.get(imgUrl)
            imgPath = f"Commands/sql/uploads/monsters/{imgName}"
            
            bestiario = discord.utils.get(ctx.guild.categories, name="Bestiário")
            
            monsterPage = await ctx.guild.create_text_channel(monster["name"], category=bestiario)
            
            # with open(imgPath, "wb") as file:
            #     file.write(response.content)
                
            monsterPageImg = await monsterPage.send(imgUrl)
            monster["img"] = monsterPageImg.content
            
            
            await msg.delete()
            await monsterImg.delete()
            return monsterPage
            
        except Exception as e:
            print(e)
            await ctx.send("[Timeout] time: 2 minutes")

    async def monsterLevel():

        try:
            msg = await ctx.send("Qual o level da criatura?")    
            monsterLevel = await client.wait_for("message", check=check, timeout=120)
            monster["lvl"] = monsterLevel.content
            
            await msg.delete()
            await monsterLevel.delete()

        except:
            await ctx.send("[Timeout] time: 2 minutes")
        
    async def monsterHp():    
        try:
            msg = await ctx.send("Qual o HP da criatura?")    
            monsterHp = await client.wait_for("message", check=check, timeout=120)
            monster["hp"] = monsterHp.content
            monster["tempHp"] = monsterHp.content
            
            await msg.delete()
            await monsterHp.delete()

        except:
            await ctx.send("[Timeout] time: 2 minutes")
        
    async def monsterAttr():
        
        async def monsterAGI():    
            try:    
                msg = await ctx.send("Qual a agilidade da criatura?")    
                monsterAgi = await client.wait_for("message", check=check, timeout=120)
                monster["agi"] = monsterAgi.content
                
                await msg.delete()
                await monsterAgi.delete()

            except:
                await ctx.send("[Timeout] time: 2 minutes")
        
        async def monsterFOR():
            try:    
                msg = await ctx.send("Qual a força da criatura?")    
                monsterFor = await client.wait_for("message", check=check, timeout=120)
                monster["for"] = monsterFor.content
                
                await msg.delete()
                await monsterFor.delete()

            except:
                await ctx.send("[Timeout] time: 2 minutes")
            
        async def monsterINT():
            try:
                msg = await ctx.send("Qual a inteligencia da criatura?")    
                monsterInt = await client.wait_for("message", check=check, timeout=120)
                monster["int"] = monsterInt.content
                
                await msg.delete()
                await monsterInt.delete()

            except:
                await ctx.send("[Timeout] time: 2 minutes")
                
        async def monsterVIG():
            try:
                msg = await ctx.send("Qual o vigor da criatura?")    
                monsterVig = await client.wait_for("message", check=check, timeout=120)
                monster["vig"] = monsterVig.content
                
                await msg.delete()
                await monsterVig.delete()
            except:
                await ctx.send("[Timeout] time: 2 minutes")
            
        async def monsterPRE():    
            try:
                msg = await ctx.send("Qual a presença da criatura?")    
                monsterPre = await client.wait_for("message", check=check, timeout=120)
                monster["pre"] = monsterPre.content
                
                await msg.delete()
                await monsterPre.delete()
            except:
                await ctx.send("[Timeout] time: 2 minutes")
        
        await monsterAGI()
        await monsterFOR()
        await monsterINT()
        await monsterPRE()
        await monsterVIG()
        
    await monsterName()
    monsterPage = await monsterImg()
    await monsterLevel()
    await monsterHp()
    await monsterAttr()
    
    embed = createMonsterEmbed()
    await monsterPage.send(embed=embed)
    saveMonster(monster)




def createMonsterEmbed():
    embed = discord.Embed(
        title=monster["name"],
        description=f"**Level:** {monster['lvl']}",
        colour=321634
    )
    embed.add_field(name="", value=f"**HP:** {monster['hp']}", inline=False)
    embed.add_field(name=" AGI", value=f"` {monster['agi']} `")
    embed.add_field(name=" FOR", value=f"` {monster['for']} `")
    embed.add_field(name=" INT", value=f"` {monster['int']} `")
    embed.add_field(name=" PRE", value=f"` {monster['pre']} `")
    embed.add_field(name=" VIG", value=f"` {monster['vig']} `")
    embed.set_image(url=monster['img'])
    return embed
    
