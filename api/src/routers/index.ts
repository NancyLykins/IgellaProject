import express from "express";
import { accountRouter } from "./accountRouter";
import { campaignRouter } from "./campaignRouter";
import { elementRouter } from "./elementRouter";

export default function Router(app: express.Application){
    accountRouter(app)
    campaignRouter(app)
    elementRouter(app)
}