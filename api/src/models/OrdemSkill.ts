import mongoose from "mongoose"
const { Schema } = mongoose

export const OrdemSkillSchema = new Schema({
    sistem: String,
    nome: String,
    atributoBase: String,
    descrição: String,
    treinamento: {
        grau: String,
        bonus: Number
    },
    requisitos: {
        carga: Boolean,
        kit: Boolean
    }
})

const OrdemSkillModel = mongoose.model('skills', OrdemSkillSchema)
export default OrdemSkillModel