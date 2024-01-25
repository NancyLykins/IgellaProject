from Commands.sql.connection import *

def takeNeededUses(rank):
    query = f"select usesToUpgrade FROM skillRankValues WHERE rank='{rank}'"
    cursor.execute(query)
    connection.commit()
    result = cursor.fetchall()
    if result:
        return result[0][0]
    else:
        return False