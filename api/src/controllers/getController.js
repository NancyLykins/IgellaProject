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



module.exports = {
    getAll,
    getNames,
    getCharacter,
    getCharacterEquips,
    getCharacterInventary,
    getCharacterAbilitys,
    getCharacterSkills,
    getCharacterHands,
}