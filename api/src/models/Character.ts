import { DataTypes, Model } from 'sequelize'
import { sequelize } from "../config/index";
import { CharacterModel, CharacterInput} from "../interfaces/CharacterInterface"
import Account from './Account';
import Campaign from './Campaign';

class Character extends Model<CharacterModel, CharacterInput> implements CharacterModel{
    public id!: number;
    public sheetId!: string;
    public campaignId!: number;
    public ownerId!: number;
}
Character.init(
    {
        id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        sheetId: {
            type: DataTypes.STRING(255),
            field: "sheet_id",
            allowNull: false,
            unique: true
        },
        campaignId: {
            type: DataTypes.INTEGER,
            field: "campaigns_id",
            allowNull: false
        },
        ownerId: {
            type: DataTypes.INTEGER,
            field: "owner_id",
            allowNull: false
        }
    },
    {
        sequelize,
        tableName: "characters",
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

export default Character