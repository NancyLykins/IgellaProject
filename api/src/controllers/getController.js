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
    return res.status(200).json(character)
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
    return res.status(200).json((item == "")? null: item)
}

async function getEffect(req, res){
    const effect = await getModeles.selectEffect(req.params.id)
    return res.status(200).json(effect)
}


module.exports = {
    getAll,
    getNames,
    getCharacter,
    getCharacterEquips,
    getCharacterInventary,
    getCharacterAbilitys,
    getCharacterSkills,
    getCharacterEquipsSlot,
    getCharacterHands,
    getItens,
    getTypedItens,
    getCharacterInventarySorted,
    getCharacterEffects,
    getEffect,
}