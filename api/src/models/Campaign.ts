import { DataTypes, Model } from 'sequelize'
import { sequelize } from "../config/index";
import { CampaignInput, CampaignModel } from '../interfaces/CampaignInterface';
import Account from './Account';

class Campaign extends Model<CampaignModel, CampaignInput> implements CampaignModel {
    public id!: number;
    public title!: string;
    public description!: string;
    public sistem!: string;
    public started!: DataView | Date;
    public master!: number;
}

Campaign.init(
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
        },
        master: {
            type: DataTypes.INTEGER,
            allowNull: false
        }
    },
    {
        sequelize,
        tableName: "campaigns",
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