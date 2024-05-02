import { Optional } from "sequelize";
export interface ElementModel{
    id: number,
    name: string,
    description: string,
    img: string | undefined,
    public: boolean,
    creator: number,
}

export interface ElementInput extends Optional<ElementModel, "id"> {}
export interface ElementOutput extends Required<ElementModel> {}