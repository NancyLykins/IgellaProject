const query = require("./query")

async function insertCharacterEffect(id, data){
    sql = `INSERT INTO characterEffects ('characterId', 'effectId', 'time') VALUES("${id}", "${data['effectId']}", "${data['time']}")`
    await query.execute(sql)
}

async function insetInventaryItem(id, itemId){
    sql = `
    INSERT INTO inventary (characterId, itemId, quant) 
    VALUES ('${id}', '${itemId}', 1)
    ON CONFLICT(characterId, itemId)
    DO UPDATE SET quant = quant + 1;
    `
    await query.execute(sql)
}


module.exports = {
    insertCharacterEffect,
    insetInventaryItem,
}
