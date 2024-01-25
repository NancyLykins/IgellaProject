import discord, time, random, asyncio

timer = 0
tick = 3

async def createSessionEmbed(msg):
    embed = discord.Embed(
        title = "Sessão iniciada",
        description= f"Data: {time.ctime()}",
        colour = int("".join(random.choice("0123456789ABCDEF") for _ in range(6)), 16)
    )
    await editSessionTime(msg, embed)
    
    
cnt = True
async def editSessionTime(msg, embed):
    view = discord.ui.View(timeout=18000)
    async def finish(interaction: discord.Interaction):
        global cnt
        cnt = False
        await interaction.message.delete()
    
    finishButton = discord.ui.Button(label="END", style=discord.ButtonStyle.red)
    finishButton.callback = finish
    view.add_item(finishButton)
    
    global timer, tick
    h = int(timer/3600)
    m = int(timer%3600/60)
    s = timer%60
    embed.set_footer(text=f"Duração: {f'{h}h {m}m {s}s' if h > 0 else f'{m}m {s}s' if m > 0 else f'{s}s'}")
    
    await msg.edit(embed=embed, view=view)
    await asyncio.sleep(tick)
    timer += tick
    if cnt != False:
        await editSessionTime(msg, embed)