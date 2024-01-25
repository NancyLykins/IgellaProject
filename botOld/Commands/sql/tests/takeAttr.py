from Commands.sql.connection import *

async def takeAttr(userId, attr):
    query = f"SELECT {attr[0]}, {attr[1]} FROM character WHERE id={userId}"
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    return result[0]
    