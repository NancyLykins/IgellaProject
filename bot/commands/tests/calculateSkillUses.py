from Commands.sql.skills.select.takeSkillRankAndUses import takeSkillRankAndUses
from Commands.sql.skills.select.takeNeededUses import takeNeededUses
from Commands.sql.skills.update.updateSkillUses import updateSkillUses
from Commands.sql.skills.update.updateSkillRank import updateSkillRank
from Commands.sql.skills.saveNewCharacterSkill import saveNewCharacterSkill

async def calculateSkillUses(ctx, skill):
    playerId = ctx.author.id
    rank, uses = takeSkillRankAndUses(playerId, skill)
    neededUses = takeNeededUses(rank)
    if(rank != "S"):
        uses += 1
        if(rank == "F" and uses == 1):
            saveNewCharacterSkill(playerId, skill)
        else:
            if(uses >= neededUses):
                match rank:
                    case "F":
                        newRank = "D"
                        
                    case "D":
                        newRank = "C"
                        
                    case "C":
                        newRank = "B"
                    
                    case "B":
                        newRank = "A"
                    
                    case "A":
                        newRank = "S"
                updateSkillRank(playerId, skill, newRank)
                await ctx.send(f">>> A pericia {skill} subiu para o rank {newRank}")
            else:
                updateSkillUses(playerId, skill, uses)

                    