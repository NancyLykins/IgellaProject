import { sequelize } from "../config/index";

import {
    Table,
    Column,
    Model,
    DataType,
} from "sequelize-typescript";

@Table({
    timestamps: false,
    tableName: "accounts",
    modelName: "Account"
})
class Account extends Model {
    @Column({
        primaryKey: true,
        type: DataType.INTEGER,
        autoIncrement: true,
    }) declare id: number;

    @Column({
        type: DataType.STRING(45),
        allowNull: false,
        unique: true
    }) declare name: string;

    @Column({
        type: DataType.STRING(255),
        allowNull: false,
        unique: true
    }) declare email: string;
        
    @Column({
        type: DataType.STRING(255),
        allowNull: false
    }) declare password: string;

    @Column({
        type: DataType.STRING(255)
    }) declare id_discord: string;
}

sequelize.addModels([Account])

export default Account;