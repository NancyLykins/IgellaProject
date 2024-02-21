const multer = require("multer")
const path = require("path")

const storage = multer.diskStorage({
    destination: (req, file, callback) => {
        let path = `public/${req.body.path}`
        callback(null, path.resolve("path"));
    },
    filename: (req, file, callback) => {
        const time = new Date().getTime();
        callback(null, `${time}_${file.originalname}`);
    },
});
module.exports = storage
