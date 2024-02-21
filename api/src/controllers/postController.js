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

async function postCharacter(req, res){
    await postModeles.insertCharacter(req.body)
    return res.status(200).json(req.body)
}

async function postExperience(req, res){
    await postModeles.insertCharacterExperience(req.params.id, req.params.xp)
    return res.status(200).json(req.params.xp)
}

async function postItem(req, res){
    const response = await postModeles.insertItem(req.body)
    return res.status(200).json(response || req.file)
}

module.exports = {
    postCharacterEffect,
    postCharacter,
    postExperience,
    postInventaryIten,
    postCharacterSkill,
    postItem,
}