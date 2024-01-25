async def waitForInt(ctx, client, message, timeout=120):
    msg = await ctx.send(f">>> {message}")

    def check(message):
        messageContent = message.content
        try:
            messageContent = int(messageContent)
            return message.author == ctx.author and message.channel == ctx.channel and isinstance(messageContent, int)
        except:
            return False
        
    try:
        response = await client.wait_for("message", check=check, timeout=timeout)
        await msg.delete()
        await response.delete()
        return response.content
        
    except Exception as e:
        await msg.delete()
        await ctx.send(f"Timeout: tempo {timeout/60} minutos")
        print(f"\n\waitForMessage:\n    {e}\n\n")