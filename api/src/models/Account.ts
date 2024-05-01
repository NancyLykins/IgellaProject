import { DataTypes, Model } from 'sequelize'
import { sequelize } from "../config/index";
import { AccountModel, AccountInput } from '../interfaces/AccountInterface';
class Account extends Model<AccountModel, AccountInput> implements AccountModel {
  public id!: number;
  public name!: string;
  public email!: string;
  public password!: string;
  public id_discord!: string;
}

Account.init({
  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true  
  },
  name: {
    type: new DataTypes.STRING(128),
    allowNull: false
  },
  email: {
    type: new DataTypes.STRING(128),
    allowNull: false
  },
  password: {
    type: new DataTypes.STRING(128),
    allowNull: false
  },
  id_discord: {
    type: new DataTypes.STRING(128),
    allowNull: false
  }
},
{
  sequelize,
  tableName: "accounts",
  timestamps: false,
  freezeTableName: true
})

export default Account