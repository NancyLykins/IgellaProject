const patchModules = require("../modules/patchModules")

async function patchCharacter(req, res){
    await patchModules.updateCharacter(req.params.id, req.body)
    return res.status(200).json()
}

async function patchCharacterInventary(req, res){
    await patchModules.updateCharacterInventary(req.params.id, req.params.item, req.body)
    return res.status(200).json()
}


async function patchCharacterHands(req, res){
    await patchModules.updateCharacterHands(req.params.id, req.params.itemId)
    return res.status(200).json()
}

async function patchCharacterEquips(req, res){
    await patchModules.updateCharacterEquips(req.params.id, req.params.slot, req.params.itemId)
    return res.status(200).json()
}

async function patchCharacterStatus(req, res){
    await patchModules.updateCharacterStatus(req.params.id, req.body)
    return res.status(200).json()
}

async function patchCharacterSkills(req, res){
    await patchModules.updateCharacterSkills(req.params.id, req.body)
    return res.status(200).json()
}

async function patchMonster(req, res){
    await patchModules.updateMonster(req.params.name, req.body)
    return res.status(200).json()
}

module.exports = {
    patchCharacterSkills,
    patchMonster,
    patchCharacter,
    patchCharacterInventary,
    patchCharacterHands,
    patchCharacterEquips,
    patchCharacterStatus
}