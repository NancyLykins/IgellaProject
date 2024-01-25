from Commands.sql.connection import *

def takeItensEmoji():
    query = "SELECT emoji FROM itens"
    cursor.execute(query)
    connection.commit()
    return cursor.fetchall()