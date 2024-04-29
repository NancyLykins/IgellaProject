import { sequelize } from "../config/index.js";
import pkg from 'sequelize';
import Account from "./Accounts.exemple/index.js";
const { DataTypes } = pkg;

const Element = sequelize.define(
    "elements",
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
        img: {
            type: DataTypes.STRING(255),
            allowNull: false
        },
        public: {
            type: DataTypes.BOOLEAN,
            defaultValue: false
        }
    },
    {
        freezeTableName: true,
        timestamps: false
    }
)

Element.belongsTo(Account, {
    as: "account",
    onDelete: "NO ACTION",
    onUpdate: "NO ACTION",
    foreignKey: {
        name: "creator",
        allowNull: false
    }
})

export default Element