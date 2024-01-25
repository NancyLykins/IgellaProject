from Commands.sql.connection import *

def takeEquipArmo(characterId):
    query=f"SELECT itens.rowId, name, emoji FROM characterBody JOIN itens ON head = itens.rowId OR chest = itens.rowId OR legs = itens.rowId OR feets = itens.rowId WHERE characterId='{characterId}'"
    cursor.execute(query)
    return cursor.fetchall()