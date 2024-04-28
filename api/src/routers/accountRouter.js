import Account from "../models/Account.js"


export function accountRouter(app){
    app.get("/accounts", async (req, res) => {
        let response = await Account.findAll()
        res.status(200).send({response})
    })
}