async def askRaceEmoji(ctx, client):
    askEmoji = await ctx.send(">>> Reaja com o emoji associado com a raça.")
    timeout = 120
    
    def check(reaction, user):
        emojiList = []
        print(reaction)
        return (user == ctx.author and reaction not in emojiList)
    
    try:
        reaction, user = await client.wait_for("reaction_add", check=check, timeout=timeout)
        await askEmoji.delete()
        return reaction.emoji
        
    except Exception as e:
        await askEmoji.delete()
        await ctx.send(f"Timeout: tempo {timeout/60} minutos")
        print(f"\n\naskRaceEmoji:\n{e}\n\n")