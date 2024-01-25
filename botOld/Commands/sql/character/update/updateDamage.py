from Commands.sql.connection import *

def updateDamage(playerId, amount, s):
    query = f"UPDATE character SET hp = hp {s} {amount} WHERE id = '{playerId}'"
    cursor.execute(query)
    connection.commit()