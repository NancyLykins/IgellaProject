import express from "express";
import elementController from "../controllers/elementController";
import multerConfig from "../config/multer"
import multer from "multer";

const upload = multer(multerConfig)

export function campaignRouter(app: express.Application){
    app.get("/campaigns", elementController.get)
    app.get("/campaigns/:id", elementController.get)
    app.post("/campaigns", upload.single('img'), elementController.post)
    app.delete("/campaigns/:id", elementController.destroy)
    app.patch("/campaigns/:id", elementController.update)
}