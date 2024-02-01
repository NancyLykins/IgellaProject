const deleteModules = require("../modules/deleteModules")

async function deleteInventaryItem(req, res){
    await deleteModules.deleteInventaryItem(req.params.id, req.params.item)
    return res.status(200)
}

async function deleteCharacterEffect(req, res){
    await deleteModules.deleteCharacterEffect(req.params.id, req.params.effectId)
    return req.status(200)
}

module.exports = {
    deleteInventaryItem,
    deleteCharacterEffect,
}