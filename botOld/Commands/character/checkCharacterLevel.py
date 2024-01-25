from Commands.sql.character.select.takeLevelAndXp import takeLevelAndXp
from Commands.sql.character.update.updateLevelAndXp import updateLevelAndXp
from Commands.sql.character.update.updatePoints import updatePoints
from Commands.sql.character.select.takePoints import takePoints

async def checkCharacterLevel(playerId, xpPerPleyer):
    level, xp = takeLevelAndXp(playerId)
    
    xpNextLvl = level*10
    xpSum = xpPerPleyer+xp
    while(xpSum >= xpNextLvl):
        level += 1
        xpSum -= xpNextLvl
        xpNextLvl = level*10
        points = takePoints(playerId)
        print(points)
        points +=1
        updatePoints(playerId, points)
    
    updateLevelAndXp(playerId, level, xpSum)
    
