from Commands.sql.connection import *

async def deleteChar(id):
    query = f"DELETE FROM character WHERE id={id}"
    cursor.execute(query)
    query = f"DELETE FROM characterSkills WHERE user={id}"
    cursor.execute(query)
    query = f"DELETE FROM inventary WHERE characterId ={id}"
    cursor.execute(query)
    cursor.execute(f"DELETE FROM characterBody WHERE characterId ='{id}'")
    connection.commit()
    cursor.execute(f"DELETE FROM characterHands WHERE characterId ='{id}'")
    connection.commit()
    cursor.execute(f"DELETE FROM characterEffects WHERE characterId ='{id}'")
    connection.commit()