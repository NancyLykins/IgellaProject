import { sequelize } from "../config/index";
import { DataTypes, Model } from 'sequelize'
import { MapElementInput, MapElementModel } from "../interfaces/MapElementInterface";
import Element from "./Element";
import Map from "./Map";

class MapElement extends Model<MapElementModel, MapElementInput> implements MapElementModel{
    public id!: number;
    public positionX!: number;
    public positionY!: number;
    public width!: number;
    public heigth!: number;
    public z_index!: number;
    public rotate!: number;
    public element_id!: number;
    public map_id!: number;
}

MapElement.init(
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
        },
        element_id: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
        map_id: {
            type: DataTypes.INTEGER,
            allowNull: false
        }
    },
    {
        sequelize,
        tableName: "map_elements",
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
        name: "map_id",
        allowNull: false
    }
})

export default MapElement