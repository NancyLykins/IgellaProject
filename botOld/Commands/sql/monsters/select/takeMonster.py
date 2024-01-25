from Commands.sql.connection import *

def takeMonster(name):
    try:
        query = f"SELECT * FROM monster WHERE name='{name}'"
        cursor.execute(query)
        monster = cursor.fetchall()
        connection.commit()
        return monster[0]
    except Exception as e:
        print(e)