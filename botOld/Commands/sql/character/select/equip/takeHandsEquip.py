from Commands.sql.connection import *

def takeHandsEquip(playerId):
    query=f"SELECT name, emoji, slot FROM characterHands JOIN itens ON rightH = itens.rowId OR leftH = itens.rowId WHERE characterId={playerId}"
    cursor.execute(query)
    return cursor.fetchall()