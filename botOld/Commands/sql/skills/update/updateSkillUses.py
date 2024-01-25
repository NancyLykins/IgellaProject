from Commands.sql.connection import *

def updateSkillUses(playerId, skill, uses):
    query = f"UPDATE characterSkills SET uses='{uses}' WHERE user='{playerId}' AND pericia='{skill}'"
    cursor.execute(query)
    connection.commit()