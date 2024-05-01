import express from "express";
import { accountRouter } from "./accountRouter";
import { campaignRouter } from "./campaignRouter";

export default function Router(app: express.Application){
    accountRouter(app)
    campaignRouter(app)
}