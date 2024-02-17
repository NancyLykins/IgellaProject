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

async function insertCharacter(data){
    let agilidade, agilidadeBuff, forca, forcaBuff, inteligencia, inteligenciaBuff, presenca, presencaBuff, vigor, vigorBuff, sql
    agilidade = data.attributes["Agilidade"]
    forca = data.attributes["Força"]
    inteligencia = data.attributes["Inteligencia"]
    presenca = data.attributes["Presença"]
    vigor = data.attributes["Vigor"]
    
    agilidadeBuff = data.buffs["agilidadeBuff"]
    forcaBuff = data.buffs["forcaBuff"]
    inteligenciaBuff = data.buffs["inteligenciaBuff"]
    presencaBuff = data.buffs["presencaBuff"]
    vigorBuff = data.buffs["vigorBuff"]
    sql = `
    INSERT INTO character
    (id, nome, idade, genero, raca, magia, classe, maxHP, hp, maxMp, mp, agilidade, agilidadeBuff, forca, forcaBuff, inteligencia, inteligenciaBuff, presenca, presencaBuff, vigor, vigorBuff)
    VALUES
    ('${data.id}', '${data.name}', '${data.age}', '${data.gender}', '${data.race}', '${data.magic}', '${data.classe}', '${data.hp}', '${data.hp}', '${data.mana}', '${data.mana}', '${agilidade}', '${agilidadeBuff}', '${forca}', '${forcaBuff}', '${inteligencia}', '${inteligenciaBuff}', '${presenca}', '${presencaBuff}', '${vigor}', '${vigorBuff}')
    `
    return await query.execute(sql)
}

async function insertCharacterExperience(name, xp){
    character = await fetch(`http://localhost:5050/characters/${name}`)
    character = (await character.json())[0]
    let xpNextLvl = parseInt(character["xpNextLvl"])
    let xpSum = parseInt(xp) + parseInt(character["xpAtual"])
    let level = parseInt(character["level"])
    let points = parseInt(character["pontosRestantes"])
    while(xpSum >= xpNextLvl){
        level += 1
        points += 1
        xpSum -= xpNextLvl
        xpNextLvl += 5
    }
    let sql = `UPDATE character SET level = '${level}', pontosRestantes = '${points}', xpAtual='${xpSum}', xpNextLvl = '${xpNextLvl}' WHERE nome LIKE '%${name}%'`
    await query.execute(sql)
}

module.exports = {
    insertCharacterEffect,
    insertCharacterExperience,
    insertInventaryItem,
    insertCharacter,
    insertCharacterSkill,
}
