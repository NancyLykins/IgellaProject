const conn = require("./connection")
const query = require("./query")
const buildUpdateSql = (id, data) =>{
    let sql = "UPDATE character SET"
    for(let key in data){
        sql += ` ${key} = ${data[key]},` 
    }
    return sql.substring(0, sql.length - 1) + ` WHERE id=${id}`
}

async function updateCharacter(id, data){
    let sql = buildUpdateSql(id, data)
    return await query.execute(sql)
}

module.exports = {
    updateCharacter
}