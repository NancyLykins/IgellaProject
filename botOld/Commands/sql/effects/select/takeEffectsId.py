from Commands.sql.connection import *

def takeEffectsId():
    query = "SELECT effectId from effects"
    cursor.execute(query)
    connection.commit()
    return cursor.fetchall()