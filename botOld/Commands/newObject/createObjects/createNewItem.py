import asyncio, requests, os, unicodedata
from Commands.newObject.createObjects.waitForMessage import waitForMessage
from Commands.newObject.createObjects.askItemInfos.askItemType import askItemType
from Commands.sql.itens.select.takeItensEmoji import takeItensEmoji



async def createNewItem(ctx, client):
    item = {
    "name": "",
    "img": "",
    "desc": "",
    "type": "",
    "action": "",
    "time": 0,
    "slot": ""
    }
    await ctx.message.delete()
    
    async def check(message):
        if(all(char.isalnum() or char == "_" for char in message.content)):
            return ctx.author == message.author and ctx.channel == message.channel
        else:
            await ctx.send("Nome do emogi")
    
    itemName = await waitForMessage(ctx, client, "Qual o nome do item?", 120)
    item["name"] = itemName
    itemName = unicodedata.normalize("NFD", itemName).encode('ascii', 'ignore').decode('utf8').casefold()
    itemName = itemName.replace(" ", "_")
    
    if(not all(char.isalnum() or char == "_" for char in itemName)):
        await ctx.send(">>> O nome só pode conter caracteres alfanuméricos e '_'")
        return False
        
    def checkEmoji(reaction, user):
        emojiList = []
        return(user == ctx.author and reaction not in emojiList)
    
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    
    askItemEmoji = await ctx.send(">>> Qual a imagem do item?\nVocê pode:\n-Reajir com um emoji\n-Enviar uma imagem\n-Enviar o link de uma imageme\n**Formatos aceitos:**JPEG/PNG/GIF")
    
    waitMessageSend = client.wait_for("message", check=check)
    waitReactionAdd = client.wait_for("reaction_add", check=checkEmoji)

    tasks = [
        waitMessageSend,
        waitReactionAdd,
    ]
    wait_tasks = [asyncio.create_task(task) for task in tasks]
    done, _ = await asyncio.wait(wait_tasks, return_when=asyncio.FIRST_COMPLETED)

    completedTask = done.pop()
    result = await completedTask

    try:
        if(isinstance(result, tuple)):
            result = result[0]
            emoji = result.emoji
            
        else:
            attachment = result.attachments
            if(attachment):
                attachment = attachment[0]
                attachmentUrl = str(attachment)
                attachmentExtendion = attachmentUrl.split("?")
                attachmentExtendion = attachmentExtendion[0].split(".")[-1]
                ext = str(attachmentExtendion)
                extAllowed = ["jpeg", "png", "gif"]
                if(ext not in extAllowed):
                    await ctx.send(">>> O formato do arquivo deve ser\n JPEG, PNG ou GIF")
                    return False
                
                imgUrl = attachment.url
            
            else:
                imgUrl = result.content
                imgUrlSplit = imgUrl.split("/")
                trigget = 0
                for urlPart in imgUrlSplit:
                    if(".png" in urlPart):
                        attachmentExtendion = "png"
                    elif(".jpeg" in urlPart):
                        attachmentExtendion = "jpeg"
                    elif(".gif" in urlPart):
                        attachmentExtendion = "gif"
                        
                
                if(attachmentExtendion is None):
                    await ctx.send(">>> O formato do arquivo deve ser\n JPEG, PNG ou GIF")
                    return False
            
            itemNameExt = f"{itemName}.{attachmentExtendion}"
            cachePath = f"Cache/{itemNameExt}"
            response = requests.get(imgUrl)
            
            with open(cachePath, "wb") as img:
                img.write(response.content)
            
            with open(cachePath, "rb")as img:  
                imgByte = img.read()
            
            if(os.path.getsize(cachePath) < 335544):
                emoji = await ctx.guild.create_custom_emoji(name=itemName, image=imgByte)
            
            else:
                await ctx.send("O tamanho da imagem é muito grande escolha outra e tente novamente")
            
            await result.delete()
         
    except:
        await ctx.send(">>> A mensagem deve conter uma imagem em anexo, um link ou uma reação")
    
    await askItemEmoji.delete()
    
    emojiList = []
    for tupla in takeItensEmoji():
        emojiList.append(tupla[0])
    
    if(emoji not in emojiList):
        item["img"] = emoji
        item["desc"] = await waitForMessage(ctx, client, "Qual a descrição do item?", 10800)      
        itemtype = await ctx.send(">>> Qual é o tipo do item?", view=askItemType(ctx, client, item))
        
    else:
        await ctx.send(">>> esse emoji já esta sendo usado, escolha outro e tente novamente")