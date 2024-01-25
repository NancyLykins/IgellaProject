from Commands.sql.connection import *

def saveCharacter(id="", name="", age="", gender="", race="", magic="", classe="", hp="", mana="", attributes="", buffs="",  skills=""):

    agilidade = attributes["Agilidade"]
    forca = attributes["Força"]
    inteligencia = attributes["Inteligencia"]
    presenca = attributes["Presença"]
    vigor = attributes["Vigor"]
    
    agilidadeBuff = buffs["agilidadeBuff"]
    forcaBuff = buffs["forcaBuff"]
    inteligenciaBuff = buffs["inteligenciaBuff"]
    presencaBuff = buffs["presencaBuff"]
    vigorBuff = buffs["vigorBuff"]


    try:
        query = f"""
        INSERT INTO character
        (id, nome, idade, genero, raca, magia, classe, maxHP, hp, maxMp, mp, agilidade, agilidadeBuff, forca, forcaBuff, inteligencia, inteligenciaBuff, presenca, presencaBuff, vigor, vigorBuff)
        VALUES
        ('{id}', '{name}', '{age}', '{gender}', '{race}', '{magic}', '{classe}', '{hp}', '{hp}', '{mana}', '{mana}', '{agilidade}', '{agilidadeBuff}', '{forca}', '{forcaBuff}', '{inteligencia}', '{inteligenciaBuff}', '{presenca}', '{presencaBuff}', '{vigor}', '{vigorBuff}')
        """
        cursor.execute(query)
        connection.commit()

    except Exception as e:
        print(e)



    try:
        for skill in skills:
            query = f"INSERT INTO characterSkills(user, pericia) VALUES ('{id}', '{skill}')"
            cursor.execute(query)
            connection.commit()

    except Exception as e:
        print(e)

    
    
    query = f"INSERT INTO inventary (characterId, itemId, quant) VALUES ({id}, 3, 0)"
    cursor.execute(query)
    connection.commit()
    
    query = f"INSERT INTO characterHands (characterId) VALUES('{id}')"
    cursor.execute(query)
    connection.commit()
    
    query = f"INSERT INTO characterBody (characterId) VALUES('{id}')"
    cursor.execute(query)
    connection.commit()