from Commands.sql.connection import *

def updateAttr(playerId, attr, attrValue):
    query = f"UPDATE character SET {attr}='{attrValue}' WHERE id='{playerId}'"
    cursor.execute(query)
    connection.commit()