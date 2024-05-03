import express from "express";
import ordemSheetController from "../controllers/ordemSheetController";


export function sheetRouter(app: express.Application){
    app.get("/sheet/ordem", ordemSheetController.get)
}