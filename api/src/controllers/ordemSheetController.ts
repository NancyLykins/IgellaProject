import { Request, Response } from "express"
import OrdemSheetModel from "../models/OrdemSheetModel";


async function get(req: Request, res: Response){
    const newSheet = new OrdemSheetModel({
        sistem: "ordem paranormal",
        nome: "teste",
        origem: "guerreiro",
        patente: "recruta",
        NEX: 5,
        deslocamento: 9,
        hp: {
            max: 20,
            atual: 18
        },
        sanidade: {
            max: 15,
            atual: 13
        },
        PE: 6,
        defesa: 10,
        atributos: {
            agilidade: 5,
            força:4,
          Numberlecto: 2,
            presença: 3,
            vigor: 1
        },
        classe: {
            nome: "uma classe ae",
            habilidades_classe: [{
                nome: "derrubar"
            }],
            trilha: {
                nome: "explorador",
                habilidades_trilha: [{
                    nome: "explorar"
                }]
            }
        },
        pericias: [
            { nome: "medicina" },
            { nome: "furtividade" }
        ] 
    })
    newSheet.save()
    return res.status(201).send({
        newSheet
    })
}

export default {
    get,
}