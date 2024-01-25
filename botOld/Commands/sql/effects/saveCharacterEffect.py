from Commands.sql.connection import *

def saveCharacterEffect(characterId, effectId, time):
    query=f"INSERT INTO characterEffects (characterId, effectId, time) VALUES('{characterId}', '{effectId}', '{time}')"
    cursor.execute(query)
    connection.commit()