from Commands.sql.connection import *

def saveItenInInventary(playerId, itemId, amount):
    query=f"INSERT INTO inventary (characterId, itemId, quant) VALUES('{playerId}', '{itemId}', '{amount}')"
    cursor.execute(query)
    connection.commit()