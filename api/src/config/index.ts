import { Sequelize } from "sequelize-typescript";
import mongoose from "mongoose"
import 'dotenv/config'

const POSTGRES_DB = process.env.POSTGRES_DB ?? "admin"
const POSTGRES_USER = process.env.POSTGRES_USER ?? "postgres"
const POSTGRES_PASSWORD = process.env.POSTGRES_PASSWORD ?? "postgres"
const POSTGRES_HOST = process.env.POSTGRES_HOST ?? "localhost"

const MONGO_DB = process.env.MONGO_DB ?? "mongodb://127.0.0.1:27017/"

export const sequelize = new Sequelize({
    database: POSTGRES_DB,
    username: POSTGRES_USER,
    password: POSTGRES_PASSWORD,
    host: POSTGRES_HOST,
    dialect: "postgres",
    models: [__dirname + "../models"],
  }
);

export const connectMongo = async () =>{
    try {
        await mongoose.connect(MONGO_DB), {
          useNewUrlParser: true,
          useUnifiedTopology: true,
        }
        console.log('MongoDB conectado com sucesso');
      } catch (error: any) {
        console.error('Erro ao conectar ao MongoDB:', error.message);
        process.exit(1);
      }
};