import { Optional } from "sequelize";
export interface MapModel{
    id: number,
    name: string,
    description: string,
    cover: string,
    campaignId: number,
}

export interface MapInput extends Optional<MapModel, "id"> {}
export interface MapOutput extends Required<MapModel> {}