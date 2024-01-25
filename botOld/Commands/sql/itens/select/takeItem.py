from Commands.sql.connection import *

def takeItem(id):
    query = f"SELECT * FROM itens WHERE rowId = {id}"
    cursor.execute(query)
    connection.commit()
    result = cursor.fetchall()
    return result[0]