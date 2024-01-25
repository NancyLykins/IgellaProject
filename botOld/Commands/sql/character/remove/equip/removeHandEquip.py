from Commands.sql.connection import *

def removeHandEquip(playerId, itemId, slot):
    if(slot == "twoH"):
        query = f"UPDATE characterHands SET rightH=Null WHERE characterId='{playerId}'"
        cursor.execute(query)
        connection.commit()
        query = f"UPDATE characterHands SET leftH=Null WHERE characterId='{playerId}'"
        cursor.execute(query)
        connection.commit()
    else:
        query = f"""
        UPDATE characterHands 
        SET 
        leftH = CASE WHEN leftH = {itemId} THEN NULL ELSE leftH END,
        rightH = CASE WHEN rightH = {itemId} THEN NULL ELSE rightH END
        WHERE characterId='{playerId}'
        """
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