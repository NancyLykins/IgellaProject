const postModeles = require("../modules/postModules")


async function postCharacterEffect(req, res){
    await postModeles.insertCharacterEffect(req.params.id, req.body)
    return res.status(200).json(res.data)
}

async function postInventaryIten(req, res){
    let status
    status = await postModeles.insertInventaryItem(req.params.id, req.params.itemId, req.body)
    return res.status(status).json({"status":status})
}

async function postCharacterSkill(req, res){
    await postModeles.insertCharacterSkill(req.params.id, req.body)
    return res.status(200).json({"status": "200"})
}

module.exports = {
    postCharacterEffect,
    postInventaryIten,
    postCharacterSkill,
}