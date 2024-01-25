from Commands.sql.connection import *

def takeEffectBuff(effectId):
    query = f"SELECT agiBuff, forBuff, intBuff, preBuff, vigBuff FROM effects WHERE effectId='{effectId}'"
    cursor.execute(query)
    connection.commit()
    result = cursor.fetchall()
    return result[0]