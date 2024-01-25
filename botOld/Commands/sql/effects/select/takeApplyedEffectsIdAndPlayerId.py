from Commands.sql.connection import *

def takeApplyedEffectsIdAndPlayerId():
    query="SELECT characterId, effectId FROM characterEffects"
    cursor.execute(query)
    connection.commit
    return cursor.fetchall()