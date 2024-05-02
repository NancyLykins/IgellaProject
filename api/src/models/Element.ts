import { sequelize } from "../config/index";
import { DataTypes, Model } from 'sequelize'
import { ElementInput, ElementModel } from "../interfaces/ElementInterface";
import Account from "./Account";

class Element extends Model<ElementModel, ElementInput> implements ElementModel{
    public id!: number;
    public name!: string;
    public description!: string;
    public img!: string | undefined;
    public public!: boolean;
    public creator!: number;
}

Element.init(
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
        },
        creator: {
            type: DataTypes.INTEGER,
            allowNull: false
        }
    },
    {
        sequelize,
        tableName: "elements",
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