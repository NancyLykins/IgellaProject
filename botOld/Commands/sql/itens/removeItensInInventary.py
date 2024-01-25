from Commands.sql.connection import *

def removeItensInInventary(playerId, itemId):
    query = f"DELETE FROM inventary WHERE characterId = '{playerId}' AND itemId ='{itemId}'"
    cursor.execute(query)
    connection.commit()