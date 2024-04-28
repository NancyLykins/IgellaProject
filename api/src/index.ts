import { App } from "./app";
import "dotenv/config";

new App().server.listen(process.env.PORT, ()=>{
    console.log(`Servidor TS rodando na porta ${process.env.PORT}`);
})