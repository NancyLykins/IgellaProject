import express from "express";
import cors from "cors";
import Router from "./routers";
import { connectMongo } from "./config";

export class App{
    public server: express.Application;
    
    constructor(allowed: string){
        this.server = express();
        this.middleware();
        this.setCors(allowed);
        this.router();
    }

    private middleware(){
        this.server.use(express.json());
        this.server.use(express.static("public"));
        connectMongo()
    }

    private setCors(allowed: string){
        this.server.use(
            cors({
                origin: `http://${allowed}`,
                methods: "GET,HEAD,PUT,PATCH,POST,DELETE",
                credentials: true,
            })
        )
    }

    public router(){
        Router(this.server);
    }
}