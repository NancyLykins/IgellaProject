import { sequelize } from "../config/index"
import { DataTypes, Model } from 'sequelize'
import { MapInput, MapModel } from "../interfaces/MapInterface.js"
import Campaign from "./Campaign.js";

class Map extends Model<MapModel, MapInput> implements MapModel{
    public id!: number;
    public name!: string;
    public description!: string;
    public cover!: string;
    public campaignId!: number;
}

Map.init(
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
        },
        campaignId: {
            type: DataTypes.INTEGER,
            allowNull: false
        }
    },
    {
        sequelize,
        tableName: "maps",
        freezeTableName: true,
        timestamps: false
    }
)

Map.belongsTo(Campaign, {
    as: "Campaign",
    onDelete: "NO ACTION",
    onUpdate: "NO ACTION",
    foreignKey: {
        field: "campaign_id",
        name: "campaignId",
        allowNull: false
    }
})

export default Map