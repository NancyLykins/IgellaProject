const query = require("./query")

async function deleteInventaryItem(id, item){
    let sql = `DELETE FROM inventary WHERE characterId='${id}' AND itemId=${item}`
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