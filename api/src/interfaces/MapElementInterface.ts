import { Optional } from "sequelize";
export interface MapElementModel{
    id: number,
    positionX: number,
    positionY: number,
    width: number,
    heigth: number,
    z_index: number,
    rotate: number,
    elementId: number,
    mapId: number
}

export interface MapElementInput extends Optional<MapElementModel, "id"> {}
export interface MapElementOutput extends Required<MapElementModel> {}