from Commands.sql.connection import *

def takeSkillRankAndUses(playerId, skill):
    query = f"select rank,uses FROM characterSkills WHERE user='{playerId}' AND pericia='{skill}'"
    cursor.execute(query)
    connection.commit()
    result = cursor.fetchall()
    if result:
        return result[0]
    else:
        return "F", 0