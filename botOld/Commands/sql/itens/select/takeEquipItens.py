from Commands.sql.connection import *

def takeEquipItens(playerId):
    query = f"SELECT rowId, name, emoji, quant FROM inventary JOIN itens ON itemId = rowId WHERE characterId='{playerId}' AND type='equipable'"
    cursor.execute(query)
    connection.commit()
    return cursor.fetchall()