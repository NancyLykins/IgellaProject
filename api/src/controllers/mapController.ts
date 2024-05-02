import fs from "fs"
import {Request, Response, response} from "express"
import Map from "../models/Map";

async function get(req: Request, res: Response){
    try {
        let data: any;
        if(req.params.id == undefined){
            data = await Map.findAll()
        } else {
            data = await Map.findOne({ where: {id: req.params.id}})
        }
        if(data === null){
            return res.status(404).send(
                {
                    type: "not found",
                    message: `The element with the id '${req.params.id}' was not found`
                }
            )
        }
        return res.status(200).send(
            { 
                type: "success",
                message: "Map found",
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
        if(body.campaign_id === undefined) missedParameters.push("campaign_id")
        if(req.file?.filename === undefined) missedParameters.push("cover")
        if(missedParameters.length > 0){
            return res.status(400).send(
                {
                    error: "Bad Request",
                    message: "One or more required parameters wasn't passed",
                    missed: missedParameters
                }        
            )
        }
        const element = await Map.create({
            name: body.name,
            description: body?.description,
            cover: req.file?.filename,
            campaign_id: body?.campaign_id
        })
        return res.status(201).send(
            {
                type: "created",
                message: "Map created",
                element
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
        const elementId = req.params.id
        let imgName: any = await Map.findOne({where: {id: elementId}})
        imgName = imgName?.cover
        fs.unlink(`public/${imgName}` , (err: any)=>{
            console.log(err)
        })
        await Map.destroy({ where: {"id": elementId}})
        return res.status(200).send(
            {
                type: "ok",
                message: `The element with the id ${req.params.id} was successfully deleted`,              
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
        const elementColumns: string[] = ["id", "name", "description", "cover", "campaign_id"]
        let data: Object = req.body
        if(Object.keys(data).length <= 0 && req.file?.filename === undefined){
            return res.status(400).send(
                {
                    error: "Bad Request",
                    message: "Need to pass at least one parameter to update"
                }     
            )
        }
        for(let key of Object.keys(data)){
            if(!elementColumns.includes(key)){
                return res.status(400).send(
                    {
                        error: "Bad Request",
                        message: "One or more parameters passed is incorrected",
                    }        
                )
            }
        }
        if(req.file?.filename !== undefined){
            let imgName: any = await Map.findOne({where: {id: req.params.id}})
            imgName = imgName?.cover
            fs.unlink(`public/${imgName}` , (err: any)=>{
                console.log(err)
            })
            data = {
                ...data,
                img: req.file?.filename
            }
        }
        const rowsUpdated = await Map.update(
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
                    message: `the element with the id ${req.params.id} canno't be founded`
                }
            )
        }
        return res.status(200).send(
            {
                type: "ok",
                message: `The element with the id ${req.params.id} was successfully updated`,
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