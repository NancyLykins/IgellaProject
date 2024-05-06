import {Request, Response} from "express"
import Campaign from "../models/Campaign"
import "dotenv/config";


async function getSheets(req: Request, res: Response){
    try {
        const campaignId = req.params.campaignId
        const system = await Campaign.findOne({
            where: {id: campaignId},
            attributes: ['sistem']
        })
        const url = `http://${process.env.API_URL}/sheets/${system?.sistem}/${campaignId}`
        const data = await fetch(url)
        const response = await data.json()
        return res.status(200).send({response})

    } catch (error: any) {
        error = error.message
        if(error === "Unexpected token < in JSON at position 0"){
            error = "sheets not found for this campaign"
        }
        return res.status(500).send({
            type: "error",
            error
        })
    }    
}

export default {
    getSheets
}