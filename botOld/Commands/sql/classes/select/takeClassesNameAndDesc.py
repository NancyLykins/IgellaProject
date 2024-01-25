from Commands.sql.connection import *

def takeClassesNameAndDesc():
    query="SELECT name,desc FROM classes"
    cursor.execute(query)
    connection.commit()
    return cursor.fetchall()