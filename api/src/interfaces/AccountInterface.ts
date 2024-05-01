import { Optional } from "sequelize";
export interface AccountModel{
    id: number;
    name: string;
    email: string;
    password: string;
    id_discord: string;
  }

export interface AccountInput extends Optional<AccountModel, "id"> {}
export interface AccountOutput extends Required<AccountModel> {}