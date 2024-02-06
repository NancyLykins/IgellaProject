const patchModules = require("../modules/patchModules")

async function patchCharacter(req, res){
    await patchModules.updateCharacter(req.params.id, req.body)
    return res.status(200).json(req.body)
}

async function patchCharacterInventary(req, res){
    await patchModules.updateCharacterInventary(req.params.id, req.params.item, req.body)
    return res.status(200).json(req.body)
}


async function patchCharacterHands(req, res){
    await patchModules.updateCharacterHands(req.params.id, req.params.itemId)
    return res.status(200).json({"status": "200"})
}

async function patchCharacterEquips(req, res){
    await patchModules.updateCharacterEquips(req.params.id, req.params.slot, req.params.itemId)
    return res.status(200).json({"status": "200"})
}

async function patchCharacterStatus(req, res){
    await patchModules.updateCharacterStatus(req.params.id, req.body)
    return res.status(200).json({"status": "200"})
}

async function patchCharacterSkills(req, res){
    await patchModules.updateCharacterSkills(req.params.id, req.body)
    return res.status(200).json({"status": "200"})
}

module.exports = {
    patchCharacterSkills,
    patchCharacter,
    patchCharacterInventary,
    patchCharacterHands,
    patchCharacterEquips,
    patchCharacterStatus
}