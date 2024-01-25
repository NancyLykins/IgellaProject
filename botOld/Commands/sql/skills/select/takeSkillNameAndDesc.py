from Commands.sql.connection import *

def takeSkillNameAndDesc():
    query = "select name,desc FROM skills"
    cursor.execute(query)
    connection.commit()
    return cursor.fetchall()
    