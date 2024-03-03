import discord

async def clear(interaction: discord.Interaction, limit: str):
    if interaction.user.guild_permissions.manage_messages:
        await interaction.response.send_message("Comando executado com sucesso", ephemeral=True)
        if(isinstance(limit, str) and limit == "*"):
            messagesDelete = await interaction.channel.purge(limit=9999999999)
            deleteMessagesNumber = len(messagesDelete)
            await interaction.channel.send(f"` {deleteMessagesNumber} ` {'mensagem foi apagada' if deleteMessagesNumber == 1 else 'mensagens foram apagadas'}")
        else:
            try:
                limit = int(limit)
                messagesDelete = await interaction.channel.purge(limit=limit)
                deleteMessagesNumber = len(messagesDelete)
                await interaction.channel.send(f"` {deleteMessagesNumber} ` {'mensagem foi apagada' if deleteMessagesNumber == 1 else 'mensagens foram apagadas'}")
                
            except:
                await interaction.channel.send("Comando digitado incorretamente", ephemeral=True)
    else:
        await interaction.response.send_message("Você não tem permissão para usar esse comando", ephemeral=True)