from Commands.sql.connection import *

def takeItemQuant(playerId, itemId):
    query = f"SELECT quant FROM inventary WHERE characterId='{playerId}' and itemId = '{itemId}'"
    cursor.execute(query)
    result = cursor.fetchall()
    return result[0][0]