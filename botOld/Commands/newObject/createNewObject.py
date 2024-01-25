from Commands.newObject.createObjects.createNewRace import createNewRace
from Commands.newObject.createObjects.createNewClass import createNewClass
from Commands.newObject.createObjects.createNewSkill import createNewSkill
from Commands.newObject.createObjects.createNewItem import createNewItem
from Commands.newObject.createObjects.createNewEffect import createNewEffect

async def createNewObject(ctx, client, obj):
    obj = obj.lower()
    match obj:
        case "race":
            await createNewRace(ctx, client)
        case "class":
            await createNewClass(ctx, client)

        case "skill":
            await createNewSkill(ctx, client)
        
        case "item":
            await createNewItem(ctx, client)
        
        case "effect":
            await createNewEffect(ctx, client)
        
        case _:
            await ctx.send("Comando não existe")
            
    
