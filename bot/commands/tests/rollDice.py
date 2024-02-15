import re
from commands.tests.dices import d


async def rollDice(message):
    msg = message.content
    msg = msg.split(' ')
    diceResult = 0
    positiveDiceResult = 0
    eachDiceResult = []
    other = ""
    trigget = 0
    diceSum = 0
 
    try:
        for part in msg:
            if(part == ".roll" or part == ""):
                pass
            
            elif "d" in part:
                if part.startswith("d"):
                    faces = int(part[1:])  
                    diceResult = d(faces)
                    other +=  str(diceResult)
                    eachDiceResult.append(diceResult)
                    if(diceResult >= 0):
                        positiveDiceResult += diceResult
                        
                else:
                    part = part.split("d")
                    diceSum = 0
                    dices = int(part[0])
                    if(dices <= 100):
                        faces = int(part[1])
                        for i in range(dices):
                            diceResult = d(faces)
                            eachDiceResult.append(diceResult)
                            if(diceResult >= 0):
                                positiveDiceResult += diceResult
                            diceSum += diceResult
                            
                        other += str(diceSum)
                    
                    else:
                        await message.channel.send(f"{message.author.mention}```Tá quendo explodir meu pc FDP???```")
                        return False
                
            else:
                try:
                    partInt = int(part)
                    if(isinstance(partInt, int)):
                        trigget = 1 
                except:
                    pass

                other += part
        
        if(trigget == 1):  
            trigget = 0
            print(f"Thisssss: {other}")
            result = eval(other)
            print(f"Thosssss: {result}")
            other = result - positiveDiceResult
            
            if(other >= 0):
                other = f"+ {other}"
            else:
                other = str(other)
                other = f"{other[0]} {other[1:]}"

            await message.reply(f"` {result} ` <-- {eachDiceResult} {other}")
            
        else:
            print(other)
            result = eval(other)
            await message.reply(f"` {result} ` <-- {eachDiceResult}")

    except:
        await message.channel.send(">>> Formato de dado incorreto")