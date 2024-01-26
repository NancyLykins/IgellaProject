const conn = require("./connection");
const query = require("./query")

async function deleteInventaryItem(id, item){
    let sql = `DELETE FROM inventary WHERE characterId='${id}' AND itemId=${item}`
    return await query.execute(sql)
}

module.exports = {
    deleteInventaryItem,
}