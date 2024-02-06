const query = require("./query")

async function deleteInventaryItem(id, item){
    let sql = `UPDATE inventary SET quant = quant - 1 WHERE characterId='${id}' AND itemId=${item}`
    await query.execute(sql)
    sql = `DELETE FROM inventary WHERE characterId='${id}' AND itemId='${item}' AND quant=0`
    await query.execute(sql)
}

async function deleteCharacterEffect(id, effectId){
    let sql = `DELETE FROM characterEffects WHERE characterId='${id}' AND effectId='${effectId}'`
    await query.execute(sql)
}

module.exports = {
    deleteInventaryItem,
    deleteCharacterEffect,
}