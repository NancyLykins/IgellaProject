const postModeles = require("../modules/postModules")


async function postCharacterEffect(req, res){
    await postModeles.insertCharacterEffect(req.params.id, req.body)
    return res.status(200).json(res.data)
}

async function postInventaryIten(req, res){
    await postModeles.insetInventaryItem(req.params.id, req.params.itemId)
    return res.status(200)
}

module.exports = {
    postCharacterEffect,
    postInventaryIten,
}
