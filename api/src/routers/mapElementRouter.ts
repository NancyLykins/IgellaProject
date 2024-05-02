import express from "express";
import mapElementController from "../controllers/mapElementController";


export function mapElementRouter(app: express.Application){
    app.get("/maps/elements", mapElementController.get)
    app.get("/maps/elements/:id", mapElementController.get)
    app.post("/maps/elements", mapElementController.post)
    app.delete("/maps/elements/:id", mapElementController.destroy)
    app.patch("/maps/elements/:id", mapElementController.update)
}