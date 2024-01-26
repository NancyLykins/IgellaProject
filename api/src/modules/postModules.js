const query = require("./query")

async function insertCharacterEffect(id, data){
    console.log(data)
    sql = `INSERT INTO characterEffects ('characterId', 'effectId', 'time') VALUES("${id}", "${data['effectId']}", "${data['time']}")`
    await query.execute(sql)
}

module.exports = {
    insertCharacterEffect,
}
