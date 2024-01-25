from Commands.sql.connection import *
def removeEffect(playerId, effectId):
    query = f"DELETE FROM characterEffects WHERE characterId='{playerId}' AND effectId='{effectId}'"
    print(effectId)
    cursor.execute(query)
    connection.commit()