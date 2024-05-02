import {Request, Response} from "express"
import Account from "../models/Account"
import { EmptyStatement } from "typescript";

async function get(req: Request, res: Response){
    try {
        let data: any;
        if(req.params.id == undefined){
            data = await Account.findAll()
        } else {
            data = await Account.findOne({ where: {id: req.params.id}})
        }
        if(data === null){
            return res.status(404).send(
                {
                    type: "not found",
                    message: `The user with the id '${req.params.id}' was not found`
                }
            )
        }
        return res.status(200).send(
            { 
                type: "success",
                message: "User found",
                data 
            }
        )
    } catch (error: any) {
        return res.status(500).send(
            {
                type: "error",
                error: error.message
            }
        )
    }
}

async function post(req: Request, res: Response){
    try {
        const body: any = req.body
        let missedParameters: string[] = []
        if(body.name === undefined) missedParameters.push("name")
        if(body.email === undefined) missedParameters.push("email")
        if(body.password == undefined) missedParameters.push("password")
        if(missedParameters.length > 0){
            return res.status(400).send(
                {
                    error: "Bad Request",
                    message: "One or more required parameters wasn't passed",
                    missed: missedParameters
                }        
            )
        }

        const account = await Account.create({
            name: body.name,
            email: body.email,
            password: body.password,
            discord_id: body?.discord_id 
        })
        return res.status(201).send(
            {
                type: "created",
                message: "Account created",
                account
            }
        )
    } catch (error: any) {
        if(error.message === "Validation error"){
            return res.status(409).send({
                type: "conflict",
                message: error.errors[0].message
            })
        }
        return res.status(500).send({
            type: "error",
            error: error.message
        })
    }
}

async function destroy(req: Request, res: Response){
    try {
        const accountId = req.params.id
        await Account.destroy({ where: {"id": accountId}})
        return res.status(200).send(
            {
                type: "ok",
                message: `The account with the id ${req.params.id} was successfully deleted`,              
            }
        )
    } catch (error: any) {
        return res.status(500).send({
            type: "error",
            error: error.message
        })
    }
}

async function update(req: Request, res: Response){
    try {
        const accountColumns: string[] = ["id", "name", "email", "password", "discord_id"]
        const data: Object = req.body
        if(Object.keys(data).length <= 0){
            return res.status(400).send(
                {
                    error: "Bad Request",
                    message: "Need to pass at leas one parameter to update"
                }     
            )
        }
        for(let key of Object.keys(data)){
            if(!accountColumns.includes(key)){
                return res.status(400).send(
                    {
                        error: "Bad Request",
                        message: "One or more parameters passed is incorrected",
                    }        
                )
            }
        }
        const rowsUpdated = await Account.update(
            data,
            {
                where: {
                    "id": Number(req.params.id)
                }
            }
        )
        if(rowsUpdated[0] < 1){
            return res.status(404).send(
                {
                    type: "not funded",
                    message: `the account with the id ${req.params.id} canno't be founded`
                }
            )
        }
        return res.status(200).send(
            {
                type: "ok",
                message: `The account with the id ${req.params.id} was successfully updated`,
            }
        )
    } catch (error: any) {
        return res.status(500).send({
            type: "error",
            error: error.message
        })
    }
}

export default{
    get,
    post,
    destroy,
    update
}