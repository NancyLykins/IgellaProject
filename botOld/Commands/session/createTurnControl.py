import discord, random
from Commands.session.TURN_CONTROL import TURN_CONTROL

turn = TURN_CONTROL()
async def createTurnControl(ctx):
    global turn
    view = discord.ui.View(timeout=None)
    
    async def passturn(interaction: discord.Interaction):
        turn.increment()
        embed = createTurnEmbed()
        await interaction.response.edit_message(embed=embed)
    
    async def endTurn(interaction: discord.Interaction):
        turn.finish()
        await interaction.message.delete()
    
    turnButton = discord.ui.Button(label="PassTurn", style=discord.ButtonStyle.green)
    turnButton.callback = passturn
    view.add_item(turnButton)
    
    endTurnButton = discord.ui.Button(label="Close", style=discord.ButtonStyle.red)
    endTurnButton.callback = endTurn
    view.add_item(endTurnButton)
    
    embed = createTurnEmbed()
    await ctx.send(embed=embed, view=view)
    
    
def createTurnEmbed():
    global turn
    embed = discord.Embed(
        title=f"Turno: {turn.get()}",
        colour=int("".join(random.choice("0123456789ABCDEF") for _ in range(6)), 16)
    )
    return embed
