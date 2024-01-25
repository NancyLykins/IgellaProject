from Commands.sql.connection import *

def takeClassesName():
    query="SELECT name FROM classes"
    cursor.execute(query)
    connection.commit()
    return cursor.fetchall()
