import { Optional } from "sequelize";
export interface CharacterModel{
    id: number,
    sheetId: string,
    campaignId: number,
    ownerId: number,
}

export interface CharacterInput extends Optional<CharacterModel, "id"> {}
export interface CharacterOutput extends Required<CharacterModel> {}