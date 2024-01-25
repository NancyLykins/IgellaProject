from Commands.sql.connection import *

def takeEffectTime(characterId, effectId):
    query = f"SELECT time FROM characterEffects WHERE characterId={characterId} AND effectId={effectId}"
    cursor.execute(query)
    connection.commit()
    result = cursor.fetchall()
    return result[0][0]