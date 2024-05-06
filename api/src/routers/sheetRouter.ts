import express from "express";
import ordemSheetController from "../controllers/systemsSheetsControllers/ordemSheetController";
import sheetController from "../controllers/sheetController";


export function sheetRouter(app: express.Application){
    app.get("/campaigns/:campaignId/sheets", sheetController.getSheets)
    app.get("/sheets/ordem/:campaignId", ordemSheetController.get)
    app.post("/sheets/ordem", ordemSheetController.post)
}