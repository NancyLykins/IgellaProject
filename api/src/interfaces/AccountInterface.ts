import { Optional } from "sequelize";
export interface AccountModel{
  id: number;
  name: string;
  email: string;
  password: string;
  discord_id: string | null;
}

export interface AccountInput extends Optional<AccountModel, "id"> {}
export interface AccountOutput extends Required<AccountModel> {}