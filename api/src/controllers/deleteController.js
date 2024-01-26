const deleteModules = require("../modules/deleteModules")

async function deleteInventaryItem(req, res){
    await deleteModules.deleteInventaryItem(req.params.id, req.params.item)
    return res.status(200)
}

module.exports = {
    deleteInventaryItem,
}