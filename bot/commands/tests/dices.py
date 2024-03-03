import random, time
seed = int(time.time())
random.seed(seed)

def d(faces):
    return random.randint(1, faces)

def d20():
    return random.randint(1, 20)

def xdx(dices):
    diceResult = 0
    positiveDiceResult = 0
    eachDiceResult = []
    other = ""
    diceSum = 0
    if dices.startswith("-"):
        other += str("-")
        dices = dices[1:]

    if "d" in dices:
        if dices.startswith("d"):
            faces = int(dices[1:])
            diceResult = d(faces)
            other +=  str(diceResult)
            eachDiceResult.append(diceResult)
            if(diceResult >= 0):
                positiveDiceResult += diceResult
                
        else:
            dices = dices.split("d")
            diceSum = 0
            dicesAmount = int(dices[0])
            if(dicesAmount <= 100):
                faces = int(dices[1])
                for i in range(dicesAmount):
                    diceResult = d(faces)
                    eachDiceResult.append(diceResult)
                    if(diceResult >= 0):
                        positiveDiceResult += diceResult
                    diceSum += diceResult
                    
                other += str(diceSum)
                
    return other