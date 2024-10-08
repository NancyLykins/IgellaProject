import express from "express";
import accountController from "../controllers/accountController";


export function accountRouter(app: express.Application){
    app.get("/accounts", accountController.get)
    app.get("/accounts/:id", accountController.get)
    app.post("/accounts", accountController.post)
    app.delete("/accounts/:id", accountController.destroy)
    app.patch("/accounts/:id", accountController.update)
}