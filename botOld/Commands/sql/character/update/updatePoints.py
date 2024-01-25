from Commands.sql.connection import *

def updatePoints(playerId, points):
    query = f"UPDATE character SET pontosRestantes='{points}' WHERE id='{playerId}'"
    cursor.execute(query)
    connection.commit()