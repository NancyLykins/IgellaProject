from Commands.sql.connection import *

def takeEquipSlot(playerId, table, slot):
    if slot == "twoH":
        return False
    elif slot == "oneH": 
        query = f"select rightH, leftH from character{table} where characterId='{playerId}'"
    else:
        query = f"select {slot} from character{table} where characterId='{playerId}'"
    cursor.execute(query)
    result = cursor.fetchall()
    return result[0]