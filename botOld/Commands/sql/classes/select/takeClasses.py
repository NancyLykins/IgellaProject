from Commands.sql.connection import *

def takeClasses():
    query="SELECT * FROM classes"
    cursor.execute(query)
    connection.commit()
    return cursor.fetchall()