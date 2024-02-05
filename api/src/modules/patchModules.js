const query = require("./query")
const buildUpdateSql = (id, data, table) =>{
    let sql = `UPDATE ${table} SET`
    for(let key in data){
        let value = data[key]
        if(value[0] == "+" || value[0] == "-"){
            sql += ` ${key} = ${key} ${value},`
        } else{
            sql += ` ${key} = ${value},` 
        }
    }
    return sql.substring(0, sql.length - 1) + ` WHERE id=${id}`
}


async function updateCharacter(id, data){
    let sql = buildUpdateSql(id, data, "character")
    return await query.execute(sql)
}

async function updateCharacterInventary(id, item, data){
    let sql = buildUpdateSql(id, data, "inventary").replace('id', 'characterId') + ` AND itemId='${item}'`
    return await query.execute(sql)
}

async function updateCharacterHands(id, itemId){
    let sql = `
    UPDATE characterHands
    SET
    rightH = CASE WHEN rightH IS NULL THEN ${itemId} ELSE rightH END,
    leftH = CASE WHEN leftH IS NULL AND rightH IS NOT NULL THEN ${itemId} ELSE leftH END 
    WHERE characterId=${id}
    `
    return await query.execute(sql)
}

async function updateCharacterEquips(id, slot, itemId){
    let sql = `UPDATE characterBody SET ${slot} = '${itemId}' WHERE characterId=${id}`
    return await query.execute(sql)
}


async function updateCharacterStatus(id, data){
    let sql = buildUpdateSql(id, data, "character")
    return await query.execute(sql)
}

async function updateCharacterSkills(id, data){
    let sql = "UPDATE characterSkills SET"
    for (let key in data) {
        sql += ` ${key} = '${data[key]}',`;
    }
    sql = sql.substring(0, sql.length - 1) + ` WHERE user = '${id}'`
    return await query.execute(sql)
}

module.exports = {
    updateCharacter,
    updateCharacterSkills,
    updateCharacterInventary,
    updateCharacterHands,
    updateCharacterEquips,
    updateCharacterStatus
}