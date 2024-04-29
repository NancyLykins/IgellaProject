import { sequelize } from "../config/index.js";
import pkg from 'sequelize';
import Campaign from "./Campaign.js"
import Account from "./Accounts.exemple/index.js";
const { DataTypes } = pkg;

const Character = sequelize.define(
    "characters", 
    {
        id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        sheet_id: {
            type: DataTypes.STRING(255),
            allowNull: false,
            unique: true
        }
    },
    {
        freezeTableName: true,
        timestamps: false
    }
)

Character.belongsTo(Campaign, {
    as: "campaign",
    onDelete: "NO ACTION",
    onUpdate: "NO ACTION",
    foreignKey: {
        field: "campaign_id",
        name: "campaignId",
        allowNull: false
    }
})

Character.belongsTo(Account, {
    as: "account",
    onDelete: "NO ACTION",
    onUpdate: "NO ACTION",
    foreignKey: {
        field: "owner_id",
        name: "ownerId",
        allowNull: false
    }
})