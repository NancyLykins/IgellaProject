from Commands.sql.connection import *


def takeSkillBuffAndAttr(id, skill):
    query = f"""
SELECT buff, attr FROM characterSkills
JOIN skillRankValues ON characterSkills.rank = skillRankValues.rank
JOIN skills ON characterSkills.pericia = skills.name
WHERE user='{id}' AND pericia='{skill}'
"""
    cursor.execute(query)
    connection.commit()
    result = cursor.fetchall()
    if result == []:
        return "0"
    
    return result[0]