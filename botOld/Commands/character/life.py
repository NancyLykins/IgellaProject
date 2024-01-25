import discord
from Commands.sql.character.update.updateDamage import updateDamage
async def dealDamage(interaction, player, amount):
    updateDamage(player.id, amount, "-")
    await interaction.response.send_message(f">>> {player.name} tomou {amount} de dano")
    
async def healLife(interaction, player, amount):
    updateDamage(player.id, amount, "+")
    await interaction.response.send_message(f">>> {player.name} curou {amount} de vida")