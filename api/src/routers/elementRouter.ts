import express from "express";
import elementController from "../controllers/elementController";
import multerConfig from "../config/multer"
import multer from "multer";

const upload = multer(multerConfig)

export function elementRouter(app: express.Application){
    app.get("/elements", elementController.get)
    app.get("/elements/:id", elementController.get)
    app.post("/elements", upload.single('img'), elementController.post)
    app.delete("/elements/:id", elementController.destroy)
    app.patch("/elements/:id", upload.single('img'), elementController.update)
}