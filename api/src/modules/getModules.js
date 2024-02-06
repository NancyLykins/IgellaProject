const conn = require("./connection")
const query = require("./query")

async function selectCharacters(){
    sql = 'SELECT * FROM character'
    return await query.execute(sql)
}
async function selectNames(){
    return new Promise((res, rej) => {
        conn.all("SELECT nome FROM character", (err, result) =>{
            if(err){
                rej(err)
            } else{
                res(result)
            }
        })
    })
}
async function selectCharacter(id){
    let sql = `SELECT * FROM character WHERE id LIKE '%${id}%' or nome LIKE '%${id}%'`
    return await query.execute(sql)
}
async function selectCharacterEquips(id){
    let sql = `
SELECT * FROM characterBody
JOIN itens ON itens.rowId = characterBody.head
OR itens.rowId = characterBody.chest
OR itens.rowId = characterBody.legs
OR itens.rowId = characterBody.feets
WHERE characterId LIKE '%${id}%'
    `
    return await query.execute(sql)
    
}
async function selectCharacterInventary(id){
    let sql = `SELECT * FROM inventary JOIN itens ON itemId = rowId WHERE characterId LIKE '%${id}%'`
    return await query.execute(sql)
}
async function selectCharacterAbilitys(id){
    let sql = `SELECT * FROM abilitys WHERE characterId LIKE '%${id}%'`
    return await query.execute(sql)
}

async function selectCharacterHands(id){
    let sql = `SELECT name, emoji, slot FROM characterHands JOIN itens ON rightH = itens.rowId OR leftH = itens.rowId WHERE characterId LIKE '%${id}%'`
    return await query.execute(sql)
}

async function selectItens(id){
    let sql = `SELECT * FROM itens`
    return await query.execute(sql)
}

async function selectTypedItens(id){
    let sql = `SELECT * FROM itens WHERE type='${id}' or rowId='${id}' or name='${id}'`
    return await query.execute(sql)
}

async function selectCharacterInventarySorted(id, type){
    let sql = `SELECT * FROM inventary JOIN itens ON itemId = rowId WHERE characterId LIKE '%${id}%' AND type='${type}' or itemId='${type}'`
    return await query.execute(sql)
}

async function selectCharacterEffects(id){
    let sql = `SELECT * FROM characterEffects WHERE characterId = '${id}'`
    return await query.execute(sql)
}

async function selectCharacterEquipsSlot(id, slot){
    let sql = `select ${slot} from characterBody where characterId LIKE '%${id}%'`
    item = await query.execute(sql)
    return ((item[0][slot] == "" || item[0][slot] == null)? null: item)
}

async function selectCharacterArmo(id){
    let sql = `SELECT itens.rowId, name, emoji FROM characterBody JOIN itens ON head = itens.rowId OR chest = itens.rowId OR legs = itens.rowId OR feets = itens.rowId WHERE characterId LIKE '%${id}%'`
    return await query.execute(sql)
}


async function selectEffect(id){
    let sql = `SELECT * FROM effects WHERE effectId='${id}'`
    return await query.execute(sql)
}

async function selectCharacterStatus(id, status){
    let sql = `SELECT ${status}, ${status}Buff FROM character WHERE id LIKE '%${id}%'`
    let result = await query.execute(sql)
    values = Object.values(result[0])
    return values[0] + values[1]
}

async function selectSkillRank(id){
    let sql = `select * FROM skillRankValues WHERE rank = '${id}'`
    return await query.execute(sql)
}

async function selectSkill(skillName){
    let sql = `SELECT * FROM skills WHERE name='${skillName}'`
    return await query.execute(sql)
}

async function selectCharacterSkills(id){
    let sql = `SELECT * FROM characterSkills WHERE user LIKE '%${id}%'`
    return await query.execute(sql)
}

async function selectCharacterSkill(id, skill){
    let sql = `
    SELECT * FROM characterSkills
    JOIN skillRankValues ON characterSkills.rank = skillRankValues.rank
    JOIN skills ON characterSkills.pericia = skills.name
    WHERE user LIKE '%${id}%' AND pericia LIKE '%${skill}%'
    `
    return await query.execute(sql)
}

module.exports = {
  selectCharacter,
  selectSkill,
  selectCharacterAbilitys,
  selectCharacterStatus,
  selectSkillRank,
  selectCharacterArmo,
  selectCharacterEffects,
  selectCharacterEquips,
  selectCharacterSkills,
  selectCharacterEquipsSlot,
  selectCharacterHands,
  selectCharacterInventary,
  selectCharacterInventarySorted,
  selectCharacters,
  selectCharacterSkill,
  selectItens,
  selectNames,
  selectTypedItens,
  selectEffect,
}
