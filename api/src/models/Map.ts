import { sequelize } from "../config/index"
import { DataTypes, Model } from 'sequelize'
import { MapInput, MapModel } from "../interfaces/MapInterface"
import Campaign from "./Campaign";

class Map extends Model<MapModel, MapInput> implements MapModel{
    public id!: number;
    public name!: string;
    public description!: string;
    public cover!: string | undefined;
    public campaign_id!: number;
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
        campaign_id: {
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
        name: "campaign_id",
        allowNull: false
    }
})

export default Map