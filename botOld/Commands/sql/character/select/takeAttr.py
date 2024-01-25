from Commands.sql.connection import *

def takeAttr(playerId, attr):
    query = f"SELECT {attr} from character WHERE id='{playerId}'"
    cursor.execute(query)
    result = cursor.fetchall()
    result = result[0]
    connection.commit()
    return result[0]