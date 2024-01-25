from Commands.sql.connection import *

def takeBodyEquip(playerId):
    query=f"select name, emoji, slot from characterBody JOIN itens ON head = itens.rowId OR chest = itens.rowId OR legs = itens.rowId OR feets = itens.rowId WHERE characterId = '{playerId}'"
    cursor.execute(query)
    return cursor.fetchall()