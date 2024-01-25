from Commands.sql.connection import *

def saveEffect(effectInfos):
    effectName = effectInfos["name"]
    effectId = effectInfos["id"]
    agiBuff = effectInfos["agiBuff"]
    forBuff = effectInfos["forBuff"]
    intBuff = effectInfos["intBuff"]
    preBuff = effectInfos["preBuff"]
    vigBuff = effectInfos["vigBuff"]
    life = effectInfos["life"]
    mana = effectInfos["mana"]
    
    query=f"INSERT INTO effects (effectId, effectName, agiBuff, forBuff, intBuff, preBuff, vigBuff, life, mana) VALUES('{effectId}', '{effectName}', '{agiBuff}', '{forBuff}', '{intBuff}', '{preBuff}', '{vigBuff}', '{life}', '{mana}')"
    cursor.execute(query)
    connection.commit()