from Commands.sql.connection import *
def takeCharacterQuant(id):
    query = f"SELECT COUNT(id) FROM character WHERE id='{id}'"
    cursor.execute(query)
    result = cursor.fetchall()
    return result[0][0]