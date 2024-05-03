import { App } from "./app";
import "dotenv/config";

let web_link: string = process.env.WEB_URL ?? "localost:3030";

if(Number(web_link.split(":")[1]) == 80){ 
    web_link = web_link.split(":")[0];
}

new App(web_link).server.listen(process.env.PORT, ()=>{
    console.log(`Server running in the port: ${process.env.PORT}`);
})