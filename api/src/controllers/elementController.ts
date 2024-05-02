import fs from "fs"
import {Request, Response, response} from "express"
import Element from "../models/Element";

async function get(req: Request, res: Response){
    try {
        let data: any;
        if(req.params.id == undefined){
            data = await Element.findAll()
        } else {
            data = await Element.findOne({ where: {id: req.params.id}})
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
                message: "Element found",
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
        if(body.creator === undefined) missedParameters.push("creator")
        if(req.file?.filename === undefined) missedParameters.push("img")
        if(missedParameters.length > 0){
            return res.status(400).send(
                {
                    error: "Bad Request",
                    message: "One or more required parameters wasn't passed",
                    missed: missedParameters
                }        
            )
        }
        const element = await Element.create({
            name: body.name,
            description: body?.description,
            img: req.file?.filename,
            public: body?.public,
            creator: body.creator
        })
        return res.status(201).send(
            {
                type: "created",
                message: "Element created",
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
        let imgName: any = await Element.findOne({where: {id: elementId}})
        imgName = imgName?.img
        fs.unlink(`public/${imgName}` , (err: any)=>{
            console.log(err)
        })
        await Element.destroy({ where: {"id": elementId}})
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
        const elementColumns: string[] = ["id", "name", "description", "img", "public", "creator"]
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
            let imgName: any = await Element.findOne({where: {id: req.params.id}})
            imgName = imgName?.img
            fs.unlink(`public/${imgName}` , (err: any)=>{
                console.log(err)
            })
            data = {
                ...data,
                img: req.file?.filename
            }
        }
        const rowsUpdated = await Element.update(
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