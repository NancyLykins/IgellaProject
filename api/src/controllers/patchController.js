const patchModules = require("../modules/patchModules")

async function patchCharacter(req, res){
    await patchModules.updateCharacter(req.params.id, req.body)
    return res.status(200).json(req.body)
}

module.exports = {
    patchCharacter,
}