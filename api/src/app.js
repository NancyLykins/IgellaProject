const express = require('express')
const cors = require("cors")
const router = require("./router")
const app = express()

app.use(
    cors({
        origin: 'http://localhost:5000',
        methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
        credentials: true,
    })
)
app.use(express.static("public"))
app.use(express.json())
app.use(router)
module.exports = app