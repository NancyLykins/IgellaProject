import moment from "moment"
import {Request, Response} from "express"
import Campaign from "../models/Campaign"

async function get(req: Request, res: Response){
    try {
        let data: any;
        if(req.params.id == undefined){
            data = await Campaign.findAll()
        } else {
            data = await Campaign.findOne({ where: {id: req.params.id}})
        }
        if(data === null){
            return res.status(404).send(
                {
                    type: "not found",
                    message: `The campaign with the id '${req.params.id}' was not found`
                }
            )
        }
        return res.status(200).send(
            { 
                type: "success",
                message: "Campaign found",
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
        if(body.title === undefined) missedParameters.push("title")
        if(body.sistem === undefined) missedParameters.push("sistem")
        if(body.master == undefined) missedParameters.push("master")
        if(missedParameters.length > 0){
            return res.status(400).send(
                {
                    error: "Bad Request",
                    message: "One or more required parameters wasn't passed",
                    missed: missedParameters
                }        
            )
        }
        const campaign = await Campaign.create({
            title: body.title,
            description: body?.description,
            sistem: body.sistem,
            started: moment().toDate(),
            server_id: body?.server_id,
            master: body.master
        })
        return res.status(201).send(
            {
                type: "created",
                message: "Campaign created",
                campaign
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
        const campaignId = req.params.id
        await Campaign.destroy({ where: {"id": campaignId}})
        return res.status(200).send(
            {
                type: "ok",
                message: `The campaign with the id ${req.params.id} was successfully deleted`,              
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
        const campaignColumns: string[] = ["id", "title", "description", "sistem", "started", "server_id", "master"]
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
            if(!campaignColumns.includes(key)){
                return res.status(400).send(
                    {
                        error: "Bad Request",
                        message: "One or more parameters passed is incorrected",
                    }        
                )
            }
        }
        const rowsUpdated = await Campaign.update(
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
                    message: `the campaign with the id ${req.params.id} canno't be founded`
                }
            )
        }
        return res.status(200).send(
            {
                type: "ok",
                message: `The campaign with the id ${req.params.id} was successfully updated`,
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
    update,
}