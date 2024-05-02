import {Request, Response} from "express"
import MapElement from "../models/MapElement"

async function get(req: Request, res: Response){
    try {
        let data: any;
        if(req.params.id == undefined){
            data = await MapElement.findAll()
        } else {
            data = await MapElement.findOne({ where: {id: req.params.id}})
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
        
        if(body.positionX === undefined) missedParameters.push("positionX")
        if(body.positionY === undefined) missedParameters.push("positionY")
        if(body.width == undefined) missedParameters.push("width")
        if(body.heigth == undefined) missedParameters.push("heigth")
        if(body.width == undefined) missedParameters.push("width")
        if(body.element_id == undefined) missedParameters.push("element_id")
        if(body.map_id == undefined) missedParameters.push("map_id")
        
        if(missedParameters.length > 0){
            return res.status(400).send(
                {
                    error: "Bad Request",
                    message: "One or more required parameters wasn't passed",
                    missed: missedParameters
                }        
            )
        }

        const mapElement = await MapElement.create({
            positionX: body.positionX,
            positionY: body.positionY,
            width: body.width,
            heigth: body.heigth,
            z_index: body.z_index,
            rotate: body.rotate,
            element_id: body.element_id,
            map_id: body.map_id
        })
        return res.status(201).send(
            {
                type: "created",
                message: "map element created",
                mapElement
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
        const mapElementId = req.params.id
        await MapElement.destroy({ where: {"id": mapElementId}})
        return res.status(200).send(
            {
                type: "ok",
                message: `The map element with the id ${req.params.id} was successfully deleted`,              
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
        const mapElementColumns: string[] = ["id", "positionX", "positionY", "width", "heigth", "z_index", "rotate", "element_id", "map_id"]
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
            if(!mapElementColumns.includes(key)){
                return res.status(400).send(
                    {
                        error: "Bad Request",
                        message: "One or more parameters passed is incorrected",
                    }        
                )
            }
        }
        const rowsUpdated = await MapElement.update(
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
                    message: `the map element with the id ${req.params.id} canno't be founded`
                }
            )
        }
        return res.status(200).send(
            {
                type: "ok",
                message: `The map element with the id ${req.params.id} was successfully updated`,
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