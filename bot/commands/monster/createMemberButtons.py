import discord

async def createMemberButtons(interaction, client, callback):
    view = discord.ui.View()
    for member in interaction.guild.members:
        memberName = member.name
        clientName = ((str(client.user)).split("#"))[0]
        if(memberName != clientName):
            if member.status is not discord.Status.offline:
                button = discord.ui.Button(label=memberName, style=discord.ButtonStyle.success)
                button.callback = callback
                button.custom_id = memberName
                view.add_item(button)
            else:
                button = discord.ui.Button(label=memberName, style=discord.ButtonStyle.gray)
                button.callback = callback
                button.custom_id = memberName
                view.add_item(button)

    button = discord.ui.Button(label="EXIT", style=discord.ButtonStyle.danger)

    async def deleteVictoryMenu(interaction: discord.Interaction):
        await interaction.message.delete()

    button.callback = deleteVictoryMenu
    view.add_item(button)
    return view