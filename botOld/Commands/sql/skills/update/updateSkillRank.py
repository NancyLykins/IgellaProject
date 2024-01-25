from Commands.sql.connection import *

def updateSkillRank(playerId, skill, rank):
    query = f"UPDATE characterSkills SET rank='{rank}', uses='0' WHERE user='{playerId}' AND pericia='{skill}'"
    cursor.execute(query)
    connection.commit()