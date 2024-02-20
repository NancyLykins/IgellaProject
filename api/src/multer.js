const multer = require("multer")
const path = require("path")

const storage = multer.diskStorage({
    destination: (req, file, callback) => {
        callback(null, path.resolve("uploads"));
    },
    filename: (req, file, callback) => {
        const time = new Date().getTime();
        callback(null, `${file.originalname}_${time}`);
    },
});
module.exports = storage
