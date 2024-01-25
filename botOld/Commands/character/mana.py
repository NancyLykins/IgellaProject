from Commands.sql.character.update.updateMana import updateMana
async def spendMana(ctx, amount):
    updateMana(ctx.author.id, amount, "-")
    await ctx.send(f">>> {ctx.author.name} gastou {amount} de mana")
    
async def recoveryMana(ctx, player, amount):
    updateMana(player.id, amount, "+")
    await ctx.send(f">>> {player.name} recuperou {amount} de mana")