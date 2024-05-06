import { Request, Response } from "express"
import OrdemSheetModel from "../models/OrdemSheetModel";
import Character from "../models/Character";
import Account from "../models/Account";
import Campaign from "../models/Campaign";


async function get(req: Request, res: Response){
    try {
        const campaignId: string = req.params.campaignId
        const sheet = await OrdemSheetModel.find({"campaign": campaignId})
        if(sheet === null){
            return res.status(400).send({
                type: "bad request",
                message: "the character with the given id don't exist"
            })
        }
        return res.status(200).send({sheet})

    } catch (error: any) {
        return res.status(500).send({
            type: "error",
            error: error.message
        })
    }
}

async function post(req: Request, res: Response){
    try {
        let missedParameters: Array<String | Object> = []
        let missedAttributes: Array<String> = []
        
        if(req.body.owner === undefined) missedParameters.push("owner")
        if(req.body.campaign === undefined) missedParameters.push("campaign")

        if(req.body.name === undefined) missedParameters.push("name")
        if(req.body.origin === undefined) missedParameters.push("origin")
        if(req.body.rank === undefined) missedParameters.push("rank")
        if(req.body.nex === undefined) missedParameters.push("nex")
        if(req.body.moviment === undefined) missedParameters.push("moviment")
        if(req.body.hp === undefined) missedParameters.push("hp")
        if(req.body.sanity === undefined) missedParameters.push("sanity")
        if(req.body.pe === undefined) missedParameters.push("pe")
        if(req.body.defense === undefined) missedParameters.push("defense")
        
        if(req.body.attributes === undefined){
            missedParameters.push("attributes")
        } else {
            if(req.body.attributes.agility === undefined) missedAttributes.push("agility")
            if(req.body.attributes.strength === undefined) missedAttributes.push("strength")
            if(req.body.attributes.inteligence === undefined) missedAttributes.push("inteligence")
            if(req.body.attributes.presence === undefined) missedAttributes.push("presence")
            if(req.body.attributes.vigor === undefined) missedAttributes.push("vigor")
            
            if(missedAttributes.length > 0){ 
                let missedAttributeElements: Object = {
                    attribute: missedAttributes
                }
                missedParameters.push(missedAttributeElements)
            }
        }
        if(missedParameters.length > 0){
            return res.status(400).send({
                type: "bad request",
                message: "one or more parameters are missed",
                missedParameters
            })
        }

        const { 
            name,
            origin,
            rank,
            nex,
            moviment,
            hp,
            sanity,
            pe,
            defense,
            agility,
            strength,
            inteligence,
            presence,
            vigor,
            campaign,
            owner
        } = req.body

        console.log(name)

        const newSheet = new OrdemSheetModel({
            sistem: "Ordem Paranormal",
            name: name,
            origin: origin,
            rank: rank,
            NEX: nex,
            moviment: moviment,
            hp: {
                max: hp,
                atual: hp
            },
            sanity: {
                max: sanity,
                atual: sanity
            },
            PE: pe,
            defense: defense,
            attributes: {
                agility,
                strength,
                inteligence,
                presence,
                vigor
            },
            campaign: campaign,
            owner: owner
        })
        const sheetId = newSheet["_id"].toString()
        
        const accountCount = await Account.count(
            {where: {"id": req.body.owner}}
        )
        if(accountCount < 1){
            return res.status(400).send({
                type: "bad request",
                message: "the account passed is invalid"
            })
        }

        const campaignCount = await Campaign.count(
            {where: {"id": req.body.campaign}}
        )
        
        if(campaignCount < 1){
            return res.status(400).send({
                type: "bad request",
                message: "the campaign passed is invalid"
            })
        }

        await Character.create({
            sheetId,
            characterName: name,
            campaignId: req.body.campaign,
            ownerId: req.body.owner,
        })
        newSheet.save()

        return res.status(201).send({
            newSheet
        })
    } catch (error: any) {
        return res.status(500).send({
            type: "error",
            error: error.message
        })
    }
}

export default {
    get,
    post,
}