from Commands.sql.connection import *
def removeBodyEquip(playerId, itemId, slot):
    query = f"UPDATE characterBody SET {slot}=Null WHERE characterId='{playerId}'"
    cursor.execute(query)
    connection.commit()
    query=f"""
INSERT INTO inventary (characterId, itemId, quant) 
VALUES ('{playerId}', '{itemId}', 1)
ON CONFLICT(characterId, itemId)
DO UPDATE SET quant = quant + 1;
"""
    cursor.execute(query)
    connection.commit()