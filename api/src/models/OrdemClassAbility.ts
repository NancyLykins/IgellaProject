import mongoose from "mongoose"
const { Schema } = mongoose

export const OrdemClassAbilitySchema = new Schema({
    sistem: String,
    nome: String,
    descrição: String
})

const OrdemClassAbilityModel = mongoose.model('class_abilitys', OrdemClassAbilitySchema)
export default OrdemClassAbilityModel