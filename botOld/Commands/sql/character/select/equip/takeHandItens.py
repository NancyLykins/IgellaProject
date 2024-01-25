from Commands.sql.connection import *

def takeHandItens(characterId):
    query=f"SELECT itens.rowId, name, emoji FROM characterHands JOIN itens ON leftH = itens.rowId OR rightH = itens.rowId WHERE characterId='{characterId}'"
    cursor.execute(query)
    return cursor.fetchall()