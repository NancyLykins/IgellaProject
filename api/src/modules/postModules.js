const query = require("./query")

async function insertCharacterEffect(id, data){
    sql = `INSERT INTO characterEffects ('characterId', 'effectId', 'time') VALUES("${id}", "${data['effectId']}", "${data['time']}")`
    return await query.execute(sql)
}

async function insertInventaryItem(id, itemId){
    sql = `
    INSERT INTO inventary (characterId, itemId, quant) 
    VALUES ('${id}', '${itemId}', 1)
    ON CONFLICT(characterId, itemId)
    DO UPDATE SET quant = quant + 1;
    `
    return await query.execute(sql)
}

async function insertCharacterSkill(id, data){
    let sql = `INSERT INTO characterSkills (user, pericia, rank) VALUES('${id}', '${Object.keys(data)[0]}', 'F')`
    return await query.execute(sql)
}

module.exports = {
    insertCharacterEffect,
    insertInventaryItem,
    insertCharacterSkill,
}
