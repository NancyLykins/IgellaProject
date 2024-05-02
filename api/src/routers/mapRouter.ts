import express from "express";
import mapController from "../controllers/mapController";
import multerConfig from "../config/multer"
import multer from "multer";

const upload = multer(multerConfig)

export function mapRouter(app: express.Application){
    app.get("/maps", mapController.get)
    app.get("/maps/:id", mapController.get)
    app.post("/maps", upload.single('cover'), mapController.post)
    app.delete("/maps/:id", mapController.destroy)
    app.patch("/maps/:id", upload.single('cover'), mapController.update)
}