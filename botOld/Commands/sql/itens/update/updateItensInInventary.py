from Commands.sql.connection import *

def updateItensInInventary(playerId, itemId, quant):
    query = f"UPDATE inventary SET quant = {quant} WHERE characterId={playerId} AND itemId = {itemId}"
    cursor.execute(query)
    connection.commit()