from Commands.sql.connection import *

def updateBuffs(characterId, buffName, value):
    query = f"SELECT {buffName} FROM character WHERE id='{characterId}'"
    cursor.execute(query)
    result = cursor.fetchall()
    value += result[0][0]
    query= f"UPDATE character SET {buffName}={value} WHERE id='{characterId}'"
    cursor.execute(query)
    connection.commit()