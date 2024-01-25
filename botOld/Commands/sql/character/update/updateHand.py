from Commands.sql.connection import *

def updateHand(playerId, hand, itemId):
    query=f"""
    UPDATE characterHands
    SET
    rightH = CASE WHEN rightH IS NULL THEN {itemId} ELSE rightH END,
    leftH = CASE WHEN leftH IS NULL AND rightH IS NOT NULL THEN {itemId} ELSE leftH END    WHERE characterId={playerId}
    """
    cursor.execute(query)
    connection.commit()