const sqlite = require('sqlite3')
const dbPath = './src/modules/character.db'
const conn = new sqlite.Database(dbPath)
module.exports = conn