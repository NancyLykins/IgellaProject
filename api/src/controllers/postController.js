const postModeles = require("../modules/postModules")


async function postCharacterEffect(req, res){
    await postModeles.insertCharacterEffect(req.params.id, req.body)
    return res.status(200).json(res.data)
}

module.exports = {
    postCharacterEffect,
}
