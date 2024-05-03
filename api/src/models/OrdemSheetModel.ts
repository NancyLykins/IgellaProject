import mongoose from "mongoose"
const { Schema } = mongoose

export const OrdemSheetSchema = new Schema({
    sistem: String,
    nome: String,
    origem: String,
    patente: String,
    NEX: Number,
    deslocamento: Number,
    hp: {
        max: Number,
        atual: Number
    },
    sanidade: {
        max: Number,
        atual: Number
    },
    PE: Number,
    defesa: Number,
    atributos: {
        agilidade: Number,
        força:Number,
      Numberlecto: Number,
        presença: Number,
        vigor: Number
    },
    classe: {
        nome: String,
        habilidades_classe: [Object],
        trilha: {
            nome: String,
            habilidades_trilha: [Object]
        }
    },
    pericias: [Object],
    campaign: Number,
    owner: Number
})

const OrdemSheetModel = mongoose.model('sheets', OrdemSheetSchema)
export default OrdemSheetModel