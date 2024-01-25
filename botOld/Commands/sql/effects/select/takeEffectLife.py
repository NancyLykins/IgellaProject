from Commands.sql.connection import *

def takeEffectLife(effectId):
    query = f"SELECT life FROM effects WHERE effectId='{effectId}'"
    cursor.execute(query)
    connection.commit()
    result = cursor.fetchall()
    return result[0][0]