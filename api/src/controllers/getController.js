const getModeles = require("../modules/getModules")

async function getAll(req, res){
    const characters = await getModeles.selectCharacters()
    return res.status(200).json(characters)
}
async function getNames(req, res){
    const names = await getModeles.selectNames()
    return res.status(200).json(names)
}
async function getCharacter(req, res){
    const character = await getModeles.selectCharacter(req.params.id)
    return res.status((character != "")? 200: 404).json(character)
}
async function getCharacterEquips(req, res){
    const equips = await getModeles.selectCharacterEquips(req.params.id)
    return res.status(200).json(equips)
}
async function getCharacterArmo(req, res){
    const equips = await getModeles.selectCharacterArmo(req.params.id)
    return res.status(200).json(equips)
}
async function getCharacterInventary(req, res){
    const inv = await getModeles.selectCharacterInventary(req.params.id)
    return res.status(200).json(inv)
}
async function getCharacterAbilitys(req, res){
    const abilitys = await getModeles.selectCharacterAbilitys(req.params.id)
    return res.status(200).json(abilitys)
}
async function getCharacterSkills(req, res){
    const skills = await getModeles.selectCharacterSkills(req.params.id)
    return res.status(200).json(skills)
}
async function getCharacterHands(req, res){
    const hands = await getModeles.selectCharacterHands(req.params.id)
    return res.status(200).json(hands)
}

async function getItens(req, res){
    const itens = await getModeles.selectItens(req.params.id)
    return res.status(200).json(itens)
}

async function getTypedItens(req, res){
    const itens = await getModeles.selectTypedItens(req.params.id)
    return res.status(200).json(itens)
}

async function getCharacterInventarySorted(req, res){
    const itens = await getModeles.selectCharacterInventarySorted(req.params.id, req.params.type)
    return res.status(200).json(itens)
}

async function getCharacterEffects(req, res){
    const effects = await getModeles.selectCharacterEffects(req.params.id)
    return res.status(200).json((effects == "")? null: effects)
}

async function getCharacterEquipsSlot(req, res){
    const item = await getModeles.selectCharacterEquipsSlot(req.params.id, req.params.slot)
    return res.status(200).json(item)
}

async function getEffect(req, res){
    const effect = await getModeles.selectEffect(req.params.id)
    return res.status(200).json(effect)
}

async function getCharacterStatus(req, res){
    const status = await getModeles.selectCharacterStatus(req.params.id, req.params.status)
    return res.status(200).json(status)
}

async function getCharacterSkill(req, res){
    const skill = await getModeles.selectCharacterSkill(req.params.id, req.params.skillId)
    return res.status(200).json(skill)
}

async function getSkillRank(req, res){
    const skill = await getModeles.selectSkillRank(req.params.id)
    return res.status(200).json(skill)
}

async function getSkill(req, res){
    const skill = await getModeles.selectSkill(req.params.skillName)
    return res.status(200).json(skill)
}

async function getRace(req, res){
    const races = await getModeles.selectRaces()
    return res.status(200).json(races)
}

async function getClasses(req, res){
    const classes = await getModeles.selectClasses()
    return res.status(200).json(classes)
}

async function getClasse(req, res){
    const classe = await getModeles.selectClasse(req.params.name)
    return res.status(200).json(classe)
}

async function getSkills(req, res){
    const skills = await getModeles.selectSkills()
    return res.status(200).json(skills)
}

module.exports = {
    getAll,
    getSkills,
    getSkill,
    getClasse,
    getNames,
    getSkillRank,
    getCharacterStatus,
    getCharacter,
    getCharacterEquips,
    getCharacterSkill,
    getCharacterInventary,
    getCharacterAbilitys,
    getCharacterSkills,
    getCharacterEquipsSlot,
    getCharacterArmo,
    getClasses,
    getCharacterHands,
    getItens,
    getTypedItens,
    getCharacterInventarySorted,
    getCharacterEffects,
    getEffect,
    getRace,
}