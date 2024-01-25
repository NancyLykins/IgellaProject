from Commands.sql.connection import *
def updateLife(playerId, life):  
    query = f"UPDATE character SET hp = CASE WHEN hp + {life} <= maxHp THEN hp + {life} ELSE maxHp END WHERE id='{playerId}'"
    cursor.execute(query)
    connection.commit()
    