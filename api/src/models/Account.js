import { sequelize } from "../config/index.js";
import pkg from 'sequelize';
const { DataTypes } = pkg;

const Account = sequelize.define(
    "accounts",
    {
        id: {
            type: DataTypes.INTEGER,
            autoIncrement: true,
            primaryKey: true
        },
        name: {
            type: DataTypes.STRING(45),
            allowNull: false,
            unique: true
        },
        email: {
            type: DataTypes.STRING(255),
            allowNull: false,
            unique: true
        },
        password: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
        id_discord: {
            type: DataTypes.STRING(255)
        }
    },
    {
        freezeTableName: true,
        timestamps: false,
    }
)

export default Account