import express from "express";
import ordemSheetController from "../controllers/ordemSheetController";


export function sheetRouter(app: express.Application){
    app.get("/sheets/ordem", ordemSheetController.get)
    app.post("/sheets/ordem", ordemSheetController.post)
}