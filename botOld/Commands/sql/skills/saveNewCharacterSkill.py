from Commands.sql.connection import *
def saveNewCharacterSkill(playerId, skill):
    query = f"INSERT INTO characterSkills(user, pericia, rank, uses) VALUES ('{playerId}', '{skill}', 'F', '1')"
    cursor.execute(query)
    connection.commit()