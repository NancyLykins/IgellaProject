const express = require('express')
const cors = require("cors")
const multer = require("multer")
const router = require("./router")
const { storage } = require('./multer')
const app = express()
const upload = multer({storage: storage})
require("dotenv").config()
let web_link = (process.env.WEB_URL.split(":")[1] == 80)? process.env.WEB_URL.split(":")[0]: process.env.WEB_URL
app.use(
    cors({
        origin: `http://${web_link}`,
        methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
        credentials: true,
    })
)
app.use(express.static("public"))
app.use(express.json())
app.use(router)
module.exports = app