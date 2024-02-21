const express = require("express")
const multer = require("multer")
const getController = require("./controllers/getController")
const patchController = require("./controllers/patchController")
const deleteController = require("./controllers/deleteController")
const postController = require("./controllers/postController")
const storage = require("./multer")
const router =  express.Router()
const upload = multer({storage: storage})

router.get("/characters", getController.getAll)
router.get("/characters/names", getController.getNames)

router.get("/characters/:id", getController.getCharacter)
router.get("/characters/:id/equips", getController.getCharacterEquips)
router.get("/characters/:id/armor", getController.getCharacterArmo)
router.get("/characters/:id/equips/:slot", getController.getCharacterEquipsSlot)
router.get("/characters/:id/inventary", getController.getCharacterInventary)
router.get("/characters/:id/inventary/:type", getController.getCharacterInventarySorted)
router.get("/characters/:id/abilitys", getController.getCharacterAbilitys)
router.get("/characters/:id/skills", getController.getCharacterSkills)
router.get("/characters/:id/skills/:skillId", getController.getCharacterSkill)
router.get("/characters/:id/hands", getController.getCharacterHands)
router.get("/characters/:id/effects", getController.getCharacterEffects)
router.get("/characters/:id/:status", getController.getCharacterStatus)

router.get("/itens", getController.getItens)
router.get("/itens/:id", getController.getTypedItens)

router.get("/effects/:id", getController.getEffect)

router.get("/skills/rank/:id", getController.getSkillRank)
router.get("/skills/:skillName", getController.getSkill)

router.get("/monsters/:name", getController.getMonster)
router.get("/races", getController.getRace)
router.get("/classes", getController.getClasses)
router.get("/classes/:name", getController.getClasse)
router.get("/skills", getController.getSkills)

router.patch("/monsters/:name", patchController.patchMonster)
router.patch("/characters/:id", patchController.patchCharacter)
router.patch("/characters/:id/inventary/:item", patchController.patchCharacterInventary)
router.patch("/characters/:id/hands/:itemId", patchController.patchCharacterHands)
router.patch("/characters/:id/equips/:slot/:itemId", patchController.patchCharacterEquips)
router.patch("/characters/:id/status", patchController.patchCharacterStatus)
router.patch("/characters/:id/skills", patchController.patchCharacterSkills)

router.delete("/characters/:id/hands/:slot/:itemId", deleteController.deleteHandEquips)
router.delete("/characters/:id/inventary/:item", deleteController.deleteInventaryItem)
router.delete("/characters/:id/effects/:effectId", deleteController.deleteCharacterEffect)

router.post("/characters", postController.postCharacter)
router.post("/characters/:id/skills", postController.postCharacterSkill)
router.post("/characters/:id/inventary/:itemId", postController.postInventaryIten)
router.post("/characters/:id/effects", postController.postCharacterEffect)
router.post("/characters/:id/:xp", postController.postExperience)

router.post("/item", upload.single("file"), postController.postItem)

module.exports = router
