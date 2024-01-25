from Commands.sql.connection import *

def takeRacesNameEmojiAndDesc():
    query="SELECT name,emoji,desc FROM races"
    cursor.execute(query)
    connection.commit()
    return cursor.fetchall()