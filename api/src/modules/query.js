const conn = require("./connection")
async function execute(query){
    return new Promise((res, rej) => {
        conn.all(query, (err, result) => {
            if(err){
                rej(err)
            } else{
                res(result)
            }
        })
    })
}

module.exports = {
    execute
}