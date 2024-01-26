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
    sql = buildUpdateSql(id, data, "inventary").replace('id', 'characterId') + ` AND itemId='${item}'`
    return await query.execute(sql)
}

module.exports = {
    updateCharacter,
    updateCharacterInventary
}