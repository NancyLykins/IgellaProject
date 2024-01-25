from Commands.sql.connection import *
def takeItemId(itemName):
    query = f"SELECT rowId FROM itens WHERE name='{itemName}'"
    cursor.execute(query)
    result = cursor.fetchall()
    return result[0][0]