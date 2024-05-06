import { Optional } from "sequelize";
export interface CharacterModel{
    id: number,
    characterName: string,
    sheetId: string,
    campaignId: number,
    ownerId: number,
}

export interface CharacterInput extends Optional<CharacterModel, "id"> {}
export interface CharacterOutput extends Required<CharacterModel> {}