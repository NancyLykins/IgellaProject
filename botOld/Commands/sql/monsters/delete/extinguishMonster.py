from Commands.sql.connection import *
def extinguishMonster(monsterName):
    query=f"DELETE FROM monster WHERE name='{monsterName}'"
    cursor.execute(query)
    connection.commit()