import express from "express";
import {Request, Response} from "express";
import accountController from "../controllers/accountController";


export function accountRouter(app: express.Application){
    app.get("/accounts", accountController.get)
    app.get("/accounts/:id", accountController.get)
}