from Commands.sql.connection import *

def takeClassBuff(classe):
    query=f"SELECT agiBuff, forBuff, intBuff, preBuff, vigBuff, perBuff FROM classes WHERE name='{classe}'"
    cursor.execute(query)
    connection.commit()
    response = cursor.fetchall()
    return response[0]