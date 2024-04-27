import { sequelize } from "../config/index.js";
import pkg from 'sequelize';
import Element from "./Element.js";
import Map from "./Map.js";
const { DataTypes } = pkg;

const MapElement = sequelize.define(
    "map_elements",
    {
        id: {
            type: DataTypes.INTEGER,
            autoIncrement: true,
            primaryKey: true
        },
        positionX: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
        positionY: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
        width: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
        heigth: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
        z_index: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
        rotate: {
            type: DataTypes.INTEGER,
            defaultValue: 0
        }
    },
    {
        freezeTableName: true,
        timestamps: false
    }
)

MapElement.belongsTo(Element, {
    as: "element",
    onDelete: "NO ACTION",
    onUpdate: "NO ACTION",
    foreignKey: {
        field: "element_id",
        name: "elementId",
        allowNull: false
    }
})

MapElement.belongsTo(Map, {
    as: "map",
    onDelete: "NO ACTION",
    onUpdate: "NO ACTION",
    foreignKey: {
        field: "map_id",
        name: "mapId",
        allowNull: false
    }
})

export default MapElement