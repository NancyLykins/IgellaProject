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
    if(!isNaN(id)){
        return new Promise((res, rej) => {
            conn.all(`SELECT * FROM character WHERE id=${id}`, (err, result) =>{
                if(err){
                    rej(err)
                } else{
                    res(result)
                }
            })
        })
    } else {
        return new Promise((res, rej) => {
            conn.all(`SELECT * FROM character WHERE nome='${id}'`, (err, result)=>{
                if(err){
                    rej(err)
                } else {
                    res(result)
                }
            })
        })
    }
}
async function selectCharacterEquips(id){
    return new Promise((res, rej) => {
        conn.all(`SELECT * FROM characterBody WHERE characterId='${id}'`, (err, result) =>{
            if(err){
                rej(err)
            } else{
                res(result)
            }
        })
    })
}
async function selectCharacterInventary(id){
    let sql = `SELECT * FROM inventary JOIN itens ON itemId = rowId WHERE characterId='${id}'`
    return await query.execute(sql)
}
async function selectCharacterAbilitys(id){
    let sql = `SELECT * FROM abilitys WHERE characterId=${id}`
    return await query.execute(sql)
}
async function selectCharacterSkills(id){
    let sql = `SELECT * FROM characterSkills WHERE user=${id}`
    return await query.execute(sql)
}
async function selectCharacterHands(id){
    let sql = `SELECT name, emoji, slot FROM characterHands JOIN itens ON rightH = itens.rowId OR leftH = itens.rowId WHERE characterId='${id}'`
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
    let sql = `SELECT * FROM inventary JOIN itens ON itemId = rowId WHERE characterId='${id}' AND type='${type}'`
    return await query.execute(sql)
}

async function selectCharacterEffects(id){
    let sql = `SELECT * FROM characterEffects WHERE characterId = '${id}'`
    return await query.execute(sql)
}

module.exports = {
  selectCharacters,
  selectNames,
  selectCharacter,
  selectCharacterEquips,
  selectCharacterInventary,
  selectCharacterAbilitys,
  selectCharacterSkills,
  selectCharacterHands,
  selectItens,
  selectTypedItens,
  selectCharacterInventarySorted,
  selectCharacterEffects
}
