from Commands.sql.connection import *

def takeRacesName():
    query="SELECT name FROM races"
    cursor.execute(query)
    connection.commit()
    return cursor.fetchall()