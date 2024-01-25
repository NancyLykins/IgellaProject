from Commands.sql.connection import *

def saveSkill(name, desc, attr):
    query = f"INSERT INTO skills (name, desc, attr) VALUES('{name}', '{desc}', '{attr}')"
    cursor.execute(query)
    connection.commit()