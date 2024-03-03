const deleteModules = require("../modules/deleteModules")

async function deleteInventaryItem(req, res){
    await deleteModules.deleteInventaryItem(req.params.id, req.params.item)
    return res.status(200).json({"status": "200"})
}

async function deleteCharacterEffect(req, res){
    await deleteModules.deleteCharacterEffect(req.params.id, req.params.effectId)
    return res.status(200).json({"status": "200"})
}

async function deleteHandEquips(req, res){
    await deleteModules.deleteHandEquips(req.params.id, req.params.slot, req.params.itemId)
    return res.status(200).json({"status": "200"})
}

module.exports = {
    deleteInventaryItem,
    deleteHandEquips,
    deleteCharacterEffect,
}