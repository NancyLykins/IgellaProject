// import express from 'express'
// import cors from 'cors'
// import multer from 'multer'
// import router from "./router.js"
// import storage from "./multer.js"
// import Router from "./routers/index.js"
// import 'dotenv/config'

// const app = express()
// const upload = multer({storage: storage})

// let web_link = (process.env.WEB_URL.split(":")[1] == 80)? process.env.WEB_URL.split(":")[0]: process.env.WEB_URL
// app.use(
//     cors({
//         origin: `http://${web_link}`,
//         methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
//         credentials: true,
//     })
// )
// app.use(express.static("public"))
// app.use(express.json())
// Router(app)
// app.use(router)

// export default app

import express from "express";
import Router from "./routers";

export class App{
    public server: express.Application;
    
    constructor(){
        this.server = express();
        this.middleware();
        this.router()
    }

    private middleware(){
        this.server.use(express.json());
    }

    public router(){
        Router(this.server);
    }
}