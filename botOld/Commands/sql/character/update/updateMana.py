from Commands.sql.connection import *

def updateMana(playerId, amount, s):
    query = f"UPDATE character SET mp = mp {s} {amount} WHERE id = '{playerId}'"
    cursor.execute(query)
    connection.commit()