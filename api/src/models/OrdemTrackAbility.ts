import mongoose from "mongoose"
const { Schema } = mongoose

export const OrdemTrackAbilitySchema = new Schema({
    sistem: String,
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

const OrdemTrackAbilityModel = mongoose.model('track_abilitys', OrdemTrackAbilitySchema)
export default OrdemTrackAbilityModel