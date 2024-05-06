import express from "express";
import campaignController from "../controllers/campaignController";

export function campaignRouter(app: express.Application){
    app.get("/campaigns", campaignController.get)
    app.get("/campaigns/:id", campaignController.get)
    app.post("/campaigns", campaignController.post)
    app.delete("/campaigns/:id", campaignController.destroy)
    app.patch("/campaigns/:id", campaignController.update)
}