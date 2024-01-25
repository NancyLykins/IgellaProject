from Commands.sql.itens.select.takeItemId import takeItemId
from Commands.sql.itens.saveItenInInventary import saveItenInInventary
from Commands.sql.itens.select.takeItemQuant import takeItemQuant
from Commands.sql.itens.update.updateItensInInventary import updateItensInInventary

async def giveItem(interaction, player, item, amount):
    try:
        itemId = takeItemId(item.lower())
        playerId = player.id
        try:
            quant = int(takeItemQuant(playerId, itemId))
        except:
            quant = 0
        if(quant <= 0 or quant is None):
            saveItenInInventary(playerId, itemId, amount)
        else:
            updateItensInInventary(playerId, itemId, (amount + int(takeItemQuant(playerId, itemId))))
        await interaction.response.send_message(f"{player} recebeu {'{} {} com sucesso'.format(amount, item if amount == 1 else item + 's')}", ephemeral=True)

    except:
        await interaction.response.send_message(">>> Nenhum item encontrado", ephemeral=True)
    