import mongoose from "mongoose"
const { Schema } = mongoose

export const OrdemClassAbilitySchema = new Schema({
    nome: String,
    descrição: String
})

const Model = mongoose.model('Ordem Class Abilitys', OrdemClassAbilitySchema)
const OrdemClassAbilityModel = new Model()
export default OrdemClassAbilityModel