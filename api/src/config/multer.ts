import multer from "multer"
import path from "path";

export default {
    storage: multer.diskStorage({
        destination: path.resolve(__dirname, "..", "..", "public"),
        filename(req, file, callback){
            const time = new Date().getTime();
            callback(null, `${time}_${file.originalname}`);
        },
    })
}
