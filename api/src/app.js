const express = require('express')
const cors = require("cors")
const multer = require("multer")
const router = require("./router")
const { storage } = require('./multer')
const app = express()
const upload = multer({storage: storage})
require("dotenv").config()

app.use(
    cors({
        origin: process.env.WEB_URL,
        methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
        credentials: true,
    })
)
app.use(express.static("public"))
app.use(express.json())
app.use(router)
module.exports = app