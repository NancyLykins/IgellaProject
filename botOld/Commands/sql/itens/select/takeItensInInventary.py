from Commands.sql.connection import *

def takeItensInInventary(playerId):
    query=f"SELECT name, emoji, quant, type FROM inventary JOIN itens ON itemId = rowId WHERE characterId='{playerId}'"
    cursor.execute(query)
    connection.commit()
    return cursor.fetchall()