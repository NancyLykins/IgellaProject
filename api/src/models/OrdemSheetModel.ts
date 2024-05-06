import mongoose from "mongoose"
const { Schema } = mongoose

export const OrdemSheetSchema = new Schema({
    sistem: String,
    name: String,
    origen: String,
    rank: String,
    NEX: Number,
    moviment: Number,
    hp: {
        max: Number,
        atual: Number
    },
    sanity: {
        max: Number,
        atual: Number
    },
    PE: Number,
    defense: Number,
    attributes: {
        agility: Number,
        strength: Number,
        inteligence: Number,
        presence: Number,
        vigor: Number
    },
    classe: {
        name: String,
        class_ability: [Object],
        track: {
            name: String,
            track_ability: [Object]
        }
    },
    skills: [Object],
    campaign: Number,
    owner: Number
})

const OrdemSheetModel = mongoose.model('sheets', OrdemSheetSchema)
export default OrdemSheetModel