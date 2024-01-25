from Commands.sql.connection import *

def saveRace(raceInfos):
    raceName = raceInfos["raceName"]
    raceEmoji = raceInfos["raceEmoji"]
    raceDescription = raceInfos["raceDescription"]
    agiBuff = raceInfos["agiBuff"]
    forBuff = raceInfos["forBuff"]
    intBuff = raceInfos["intBuff"]
    preBuff = raceInfos["preBuff"]
    vigBuff = raceInfos["vigBuff"]
    perBuff = raceInfos["perBuff"]
    
    query = f"INSERT INTO races (name, emoji, desc, agiBuff, forBuff, intBuff, preBuff, vigBuff, perBuff) VALUES('{raceName}', '{raceEmoji}', '{raceDescription}', '{agiBuff}', '{forBuff}', '{intBuff}', '{preBuff}', '{vigBuff}', '{perBuff}')"
    cursor.execute(query)
    connection.commit()