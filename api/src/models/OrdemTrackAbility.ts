import mongoose from "mongoose"
const { Schema } = mongoose

export const OrdemTrackAbilitySchema = new Schema({
    nome: String,
    descrição: String,
    requerimento: [
        {
            nex: Number,
            nome: String,
            descrição: String
        }
    ]
})

const Model = mongoose.model('Ordem Track Abilitys', OrdemTrackAbilitySchema)
const OrdemTrackAbilityModel = new Model()
export default OrdemTrackAbilityModel