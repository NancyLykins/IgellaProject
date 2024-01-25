from Commands.sql.connection import *

def takeLevelAndXp(playerId):
    query = f"SELECT level,xpAtual FROM character WHERE id='{playerId}'"
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    return result[0]