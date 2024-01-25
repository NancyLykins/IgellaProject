from Commands.sql.connection import *

def saveClass(classeInfos):
    classeName = classeInfos["className"]
    classeDescription = classeInfos["classDescription"]
    agiBuff = classeInfos["agiBuff"]
    forBuff = classeInfos["forBuff"]
    intBuff = classeInfos["intBuff"]
    preBuff = classeInfos["preBuff"]
    vigBuff = classeInfos["vigBuff"]
    perBuff = classeInfos["perBuff"]
    
    query = f"INSERT INTO classes (name, desc, agiBuff, forBuff, intBuff, preBuff, vigBuff, perBuff) VALUES('{classeName}', '{classeDescription}', '{agiBuff}', '{forBuff}', '{intBuff}', '{preBuff}', '{vigBuff}', '{perBuff}')"
    cursor.execute(query)
    connection.commit()