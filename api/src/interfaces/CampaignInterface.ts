import { Optional } from "sequelize";

export interface CampaignModel{
    id: number,
    title: string,
    description: string,
    sistem: string,
    started: DataView | Date,
    server_id: string | null,
    master: number
}

export interface CampaignInput extends Optional<CampaignModel, "id"> {}
export interface CampaignOutput extends Required<CampaignModel> {}