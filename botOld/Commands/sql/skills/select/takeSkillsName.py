from Commands.sql.connection import *

def takeSkillsName():
    query = "select name FROM skills"
    cursor.execute(query)
    connection.commit()
    return cursor.fetchall()