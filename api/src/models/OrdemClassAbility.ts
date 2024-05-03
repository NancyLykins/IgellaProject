import mongoose from "mongoose"
const { Schema } = mongoose

export const OrdemClassAbilitySchema = new Schema({
    nome: String,
    descrição: String
})

const OrdemClassAbilityModel = mongoose.model('Ordem Class Abilitys', OrdemClassAbilitySchema)
export default OrdemClassAbilityModel