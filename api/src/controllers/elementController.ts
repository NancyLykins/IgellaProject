import moment from "moment"
import {Request, Response} from "express"
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
        const ElementNotNull: string[] = ["name", "img", "creator"]
        const body: any = req.body
        let missedParameters: string[] = []
        for(let i = 0; i <= ElementNotNull.length; i++){
            if(!ElementNotNull.includes(Object.keys(body)[i]) && i < ElementNotNull.length){
                missedParameters.push(Object.keys(body)[i])
            }
            if(ElementNotNull.length == i && missedParameters.length > 0){
                return res.status(400).send(
                    {
                        error: "Bad Request",
                        message: "One or more required parameters wasn't passed",
                        missed: missedParameters
                    }        
                )
            }
        }
        console.log(missedParameters)
        const element = await Element.create({
            name: body.name,
            description: body?.description,
            img: body.img,
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
            if(!elementColumns.includes(key)){
                return res.status(400).send(
                    {
                        error: "Bad Request",
                        message: "One or more parameters passed is incorrected",
                    }        
                )
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