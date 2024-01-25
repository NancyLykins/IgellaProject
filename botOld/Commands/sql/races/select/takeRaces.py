from Commands.sql.connection import *

def takeRaces():
    query="SELECT * FROM races"
    cursor.execute(query)
    connection.commit()
    return cursor.fetchall()