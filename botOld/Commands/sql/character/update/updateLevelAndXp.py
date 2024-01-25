from Commands.sql.connection import *

def updateLevelAndXp(playerId, newLvl, newXp):
    query = f"UPDATE character SET level={newLvl}, xpAtual={newXp} WHERE id='{playerId}'"
    cursor.execute(query)
    connection.commit()