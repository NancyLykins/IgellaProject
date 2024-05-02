import mongoose from "mongoose"
const { Schema } = mongoose

export const OrdemClassAbilitySchema = new Schema({
    nome: String,
    descrição: String
})