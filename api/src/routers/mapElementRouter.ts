import express from "express";
import mapElementController from "../controllers/mapElementController";


export function mapElementRouter(app: express.Application){
    app.get("/map/elements", mapElementController.get)
    app.get("/map/elements/:id", mapElementController.get)
    app.post("/map/elements", mapElementController.post)
    app.delete("/map/elements/:id", mapElementController.destroy)
    app.patch("/map/elements/:id", mapElementController.update)
}