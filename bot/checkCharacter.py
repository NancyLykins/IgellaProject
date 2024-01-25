from Commands.sql.character.select.takeCharacterQuant import takeCharacterQuant
async def checkCharacterExist(ctx):
    quant = takeCharacterQuant(ctx.author.id)
    if quant == 0:
        await ctx.send(">>> Você não tem um personagem criado")

async def checkCharacterNExist(ctx):
    quant = takeCharacterQuant(ctx.author.id)
    if quant == 1:
        await ctx.send(">>> Você já tem um personagem criado")
        return 1
    else:
        return 0
        