import discord

async def sayText(interaction: discord.Interaction, title, message, footer):
    if interaction.user.id == 663141450564894750:
        await interaction.channel.send(title)
        await interaction.channel.send(message)
        await interaction.channel.send(footer)
        await interaction.response.send_message("Mensagem enviada com sucesso!", ephemeral=True)
    else:
        await interaction.response.send_message("Você não tem permissão de usar esse comando", ephemeral=True)
