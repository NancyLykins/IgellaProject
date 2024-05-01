import { Optional } from "sequelize";

export interface CampaignModel{
    id: number,
    title: string,
    description: string,
    sistem: string,
    started: DataView,
    master: number
}

export interface CampaignInput extends Optional<CampaignModel, "id"> {}
export interface CampaignOutput extends Required<CampaignModel> {}