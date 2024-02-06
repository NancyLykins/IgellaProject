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

async function deleteHandEquips(id, slot, itemId){
    let sql
    if (slot == "twoH") {
        sql = `UPDATE characterHands SET rightH=Null, leftH=Null WHERE characterId='${id}'`
    } else {
        sql = `
        UPDATE characterHands 
        SET 
        leftH = CASE WHEN leftH = '${itemId}' THEN NULL ELSE leftH END,
        rightH = CASE WHEN rightH = '${itemId}' THEN NULL ELSE rightH END
        WHERE characterId='${id}'
        `
    }
    console.log(sql)
    await query.execute(sql)
}

module.exports = {
    deleteInventaryItem,
    deleteCharacterEffect,
    deleteHandEquips,
}