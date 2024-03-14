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
    let sql = `SELECT * FROM characterHands JOIN itens ON rightH = itens.rowId OR leftH = itens.rowId WHERE characterId LIKE '%${id}%'`
    return await query.execute(sql)
}

async function selectItens(id){
    let sql = `SELECT * FROM itens`
    return await query.execute(sql)
}

async function selectTypedItens(id){
    id = id.replace(/\+/g, " ")
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

async function selectRaces(){
    let sql = "SELECT * FROM races"
    return await query.execute(sql) 
}

async function selectClasses(){
    let sql = "SELECT * FROM classes"
    return await query.execute(sql)
}

async function selectClasse(className){
    let sql = `SELECT * FROM classes WHERE name = '${className}'`
    return await query.execute(sql)
}

async function selectSkills(){
    sql = "SELECT * FROM skills"
    return await query.execute(sql)
}

async function selectMonster(monster){
    sql = `SELECT * FROM monster WHERE name = '${monster}'`
    return await query.execute(sql)
}

async function selectMissions(missionQuant){
    let missions = ["Test"]
    let mission = {}
    let missionExemple = {
        "nomeMissao1": {
            "rank": "D",
            "desc": "",
            "local": "",
            "descOpc": "",
            "grupo": "",
            "contratante": "",
            "recompensa": ""
        },
        "nomeMissao2": {
            "rank": "C",
            "desc": "",
            "local": "",
            "descOpc": "",
            "grupo": "",
            "contratante": "",
            "recompensa": ""
        },
        "nomeMissao3": {
            "rank": "B",
            "desc": "",
            "local": "",
            "descOpc": "",
            "grupo": "",
            "contratante": "",
            "recompensa": ""
        },
        "nomeMissao4": {
            "rank": "A",
            "desc": "",
            "local": "",
            "descOpc": "",
            "grupo": "",
            "contratante": "",
            "recompensa": ""
        },
        "nomeMissao5": {
            "rank": "S",
            "desc": "",
            "local": "",
            "descOpc": "",
            "grupo": "",
            "contratante": "",
            "recompensa": ""
        },
        "nomeMissao6": {
            "rank": "E",
            "desc": "",
            "local": "",
            "descOpc": "",
            "grupo": "",
            "contratante": "",
            "recompensa": ""
        }
    }
    let randomRanks = []
    for(let i = 0; i < missionQuant; i++){
        let  ranks = [
            "S",
            "A", "A",
            "B", "B", "B",
            "C", "C", "C", "C",
            "D", "D", "D", "D", "D",
            "E", "E", "E", "E", "E", "E",
            "F", "F", "F", "F", "F", "F", "F",
        ]
        randomRanks.push(ranks[Math.floor(Math.random() * ranks.length)])
    }
    let rand, missionKey, j = 0
    for(let i = 0; i < missionQuant; i++){
        let cache = [], j = 0
        while(true){
            let k = 0
            console.log(`Tentativa ${j}`)
            rand = Math.floor(Math.random() * Object.keys(missionExemple).length)
            if(cache.includes(rand)){
                console.log(`${rand} alreary is in cache:\n{${cache}}\ntrying to find other`)
                while(cache.includes(rand)){
                    rand = Math.floor(Math.random() * Object.keys(missionExemple).length)
                    k += 1
                    if(!(cache.includes(rand))) {
                        cache.push(rand)
                        console.log(`The new rand is: ${rand}`)
                    }
                    if(k >= Object.keys(missionExemple).length) break
                }
            } else {
                cache.push(rand)
            }         
            missionKey = Object.keys(missionExemple)
            missionKey = missionKey[rand]
            console.log(`Random rank: ${randomRanks}\nFiding pattern:`)
            console.log(missionExemple[missionKey].rank)
            console.log("MIR: "+ randomRanks.includes(missionExemple[missionKey].rank))
            if(randomRanks.includes(missionExemple[missionKey].rank)){
                let position
                missions.push(missionExemple[missionKey])
                position = randomRanks.lastIndexOf(missionExemple[missionKey].rank)
                console.log(`Position: ${position}`)
                randomRanks = randomRanks.splice(randomRanks, randomRanks+1)
                break
            }
            j += 1
            console.log("\n\n")
            if(cache.length >= Object.keys(missionExemple).length) break
        }
    }
    return missions
}

module.exports = {
  selectCharacter,
  selectSkills,
  selectSkill,
  selectMonster,
  selectClasse,
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
  selectRaces,
  selectClasses,
  selectMissions
}