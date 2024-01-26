const express = require('express')
const getController = require("./controllers/getController")
const patchController = require("./controllers/patchController")
const deleteController = require("./controllers/deleteController")
const postController = require("./controllers/postController")
const router =  express.Router()


router.get("/characters", getController.getAll)
router.get("/characters/names", getController.getNames)

router.get("/characters/:id", getController.getCharacter)
router.get("/characters/:id/equips", getController.getCharacterEquips)
router.get("/characters/:id/inventary", getController.getCharacterInventary)
router.get("/characters/:id/inventary/:type", getController.getCharacterInventarySorted)
router.get("/characters/:id/abilitys", getController.getCharacterAbilitys)
router.get("/characters/:id/skills", getController.getCharacterSkills)
router.get("/characters/:id/hands", getController.getCharacterHands)
router.get("/characters/:id/effects", getController.getCharacterEffects)

router.get("/itens", getController.getItens)
router.get("/itens/:id", getController.getTypedItens)


router.patch("/characters/:id", patchController.patchCharacter)
router.patch("/characters/:id/inventary/:item", patchController.patchCharacterInventary)

router.delete("/characters/:id/inventary/:item", deleteController.deleteInventaryItem)

router.post("/characters/:id/effects", postController.postCharacterEffect)
module.exports = router