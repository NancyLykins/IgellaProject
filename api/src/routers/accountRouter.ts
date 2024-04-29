import express from "express";
import {Request, Response} from "express";
import Account from "../models/Account"


export function accountRouter(app: express.Application){
    app.get("/accounts", async (req: Request, res: Response) => {
        let response = await Account.findAll()
        res.status(200).send({response})
    })
}