const conn = require("./connection");
const query = require("./query")

async function selectCharacters(){
    return new Promise((res, rej) => {
        conn.all('SELECT * FROM character', (err, result) => {
            if(err){
                rej(err)
            } else{
                res(result)
            }
        })
    })
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
    let sql = `SELECT * FROM characterHands WHERE characterId='${id}'`
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
}
