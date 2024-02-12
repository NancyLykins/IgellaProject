const query = require("./query")

async function insertCharacterEffect(id, data){
    sql = `INSERT INTO characterEffects ('characterId', 'effectId', 'time') VALUES("${id}", "${data['effectId']}", "${data['time']}")`
    return await query.execute(sql)
}

async function insertInventaryItem(id, item, body){
    let itemId = null
    let amount
    if(Object.keys(body).length === 0){
        amount = 1
    } else{
        amount = body[item]
    }
    itemId = parseInt(item)
    if(isNaN(itemId)){
        itemId = (await query.execute(`SELECT rowId FROM itens WHERE name = '${item}'`))[0]
        if(itemId == ""){
            return 404
        }
        itemId = itemId["rowId"]
    }

    sql = `
    INSERT INTO inventary (characterId, itemId, quant) 
    VALUES ('${id}', '${itemId}', '${amount}')
    ON CONFLICT(characterId, itemId)
    DO UPDATE SET quant = quant + ${amount};
    `

    await query.execute(sql)
    return 200
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
