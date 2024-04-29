import express from "express";
import { accountRouter } from "./accountRouter";


export default function Router(app: express.Application){
    accountRouter(app);
}