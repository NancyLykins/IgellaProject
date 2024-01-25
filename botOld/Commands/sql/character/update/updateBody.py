from Commands.sql.connection import *

def updateBody(playerId, slot, itemId):
    query=f"UPDATE characterBody SET {slot} = '{itemId}' WHERE characterId={playerId}"
    cursor.execute(query)
    connection.commit()