import { sequelize } from "../config/index.js";
import pkg from 'sequelize';
import Account from "./Account.js";
const { DataTypes } = pkg;

const Campaign = sequelize.define(
    "campaigns",
    {
        id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        title: {
            type: DataTypes.STRING(45),
            allowNull: false
        },
        description: {
            type: DataTypes.TEXT
        },
        sistem: {
            type: DataTypes.STRING(45),
            allowNull: false
        },
        started: {
            type: DataTypes.DATE,
            allowNull: false
        }
    },
    {
        freezeTableName: true,
        timestamps: false
    }
)

Campaign.belongsTo(Account, {
    as: "cargo",
    onDelete: 'NO ACTION',
    onUpdate: 'NO ACTION',
    foreignKey: {
        name: 'master',
        allowNull: false,
    },
});

export default Campaign