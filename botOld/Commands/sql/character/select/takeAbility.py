from Commands.sql.connection import *
def takeAbility(id):
    query = f"SELECT name, desc from abilitys WHERE characterId='{id}'"
    cursor.execute(query)
    return cursor.fetchall()
    