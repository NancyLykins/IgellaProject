from Commands.sql.connection import *

def takeItemAction(itemId):
    query = f"SELECT action FROM itens WHERE rowId = {itemId}"
    cursor.execute(query)
    result = cursor.fetchall()
    return result[0][0]