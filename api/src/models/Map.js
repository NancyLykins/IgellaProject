import { sequelize } from "../config/index.js"
import pkg from 'sequelize'
import Campaign from "./Campaign.js"
const { DataTypes } = pkg


const Map = sequelize.define(
    "maps",
    {
        id: {
            type: DataTypes.INTEGER ,
            primaryKey: true,
            autoIncrement: true
        },
        name: {
            type: DataTypes.STRING(45),
            allowNull: false
        },
        description: {
            type: DataTypes.TEXT
        },
        cover: {
            type: DataTypes.STRING(255)
        }
    },
    {
        freezeTableName: true,
        timestamps: false
    }
)

Map.belongsTo(Campaign, {
    as: Campaign,
    onDelete: "NO ACTION",
    onUpdate: "NO ACTION",
    foreignKey: {
        field: "campaign_id",
        name: "campaignId",
        allowNull: false
    }
})

export default Map