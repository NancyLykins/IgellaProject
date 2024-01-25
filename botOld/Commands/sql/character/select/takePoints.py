from Commands.sql.connection import *

def takePoints(playerId):
    query = f"SELECT pontosRestantes FROM character WHERE id='{playerId}'"
    cursor.execute(query)
    result = cursor.fetchall()
    result =  result[0]
    connection.commit()
    return result[0]