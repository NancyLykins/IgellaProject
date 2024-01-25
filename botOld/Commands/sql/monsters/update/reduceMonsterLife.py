from Commands.sql.connection import *

def reduceMonsterLife(monsterName, newLife):
    query = f"UPDATE monster SET tempHp='{newLife}' WHERE name='{monsterName}'"
    cursor.execute(query)
    connection.commit()