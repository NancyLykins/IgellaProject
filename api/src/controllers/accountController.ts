import {Request, Response} from "express"
import Account from "../models/Account"

async function get(req: Request, res: Response){
    try {
        let result: any;
        if(req.params.id == undefined){
            result = await Account.findAll()
        } else {
            result = await Account.findOne({ where: {id: req.params.id}})
        }

        return res.status(200).send({ result })
    } catch (error: any) {
        console.log(error.message)
    }
}


export default{
    get
}