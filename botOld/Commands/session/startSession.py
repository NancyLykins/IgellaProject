import discord
from Commands.session.createSessionEmbed import createSessionEmbed
from Commands.session.createTurnControl import createTurnControl

async def startSession(ctx, function):
    await ctx.message.delete()
    match function:
        case "timer":
            msg = await ctx.send(".")
            await createSessionEmbed(msg)
        case "controls":
            await createTurnControl(ctx)
        case _:
            await ctx.send(">>> Comando inválido")