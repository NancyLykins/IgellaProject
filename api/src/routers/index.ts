import express from "express";
import { accountRouter } from "./accountRouter";
import { campaignRouter } from "./campaignRouter";
import { elementRouter } from "./elementRouter";
import { mapRouter } from "./mapRouter";
import { mapElementRouter } from "./mapElementRouter";

export default function Router(app: express.Application){
    accountRouter(app)
    campaignRouter(app)
    elementRouter(app)
    mapElementRouter(app)
    mapRouter(app)
}