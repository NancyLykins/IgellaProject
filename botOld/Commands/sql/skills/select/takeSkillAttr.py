from Commands.sql.connection import *

def takeSkillAttr(skill):
    query = f"select attr FROM skills WHERE name='{skill}'"
    cursor.execute(query)
    connection.commit()
    result = cursor.fetchall()
    if result:
        return result[0][0]
    else:
        return False