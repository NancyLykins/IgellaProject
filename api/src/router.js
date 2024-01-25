const express = require('express')
const getController = require("./controllers/getController")
const patchController = require("./controllers/patchController")
const router =  express.Router()


router.get("/characters", getController.getAll)
router.get("/characters/names", getController.getNames)

router.get("/characters/:id", getController.getCharacter)
router.get("/characters/:id/equips", getController.getCharacterEquips)
router.get("/characters/:id/inventary", getController.getCharacterInventary)
router.get("/characters/:id/abilitys", getController.getCharacterAbilitys)
router.get("/characters/:id/skills", getController.getCharacterSkills)
router.get("/characters/:id/hands", getController.getCharacterHands)

router.patch("/characters/:id", patchController.patchCharacter)


module.exports = router