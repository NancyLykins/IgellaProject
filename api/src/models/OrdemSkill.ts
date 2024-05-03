import mongoose from "mongoose"
const { Schema } = mongoose

export const OrdemSkillSchema = new Schema({
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

const Model = mongoose.model('Ordem Skills', OrdemSkillSchema)
const OrdemSkillModel = new Model()
export default OrdemSkillModel