import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("API_URL")
header = {'Content-type': 'application/json'}

async def calculateSkillUses(ctx, skill):
    id = ctx.author.id
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}/characters/{id}/skills/{skill}") as response:
            data = await response.json()

        if data != []:
            data = data[0]
            rank = data["rank"]
            uses = data["uses"] + 1
            if(rank != "S"):
                async with session.get(f"{url}/skills/rank/{rank}") as response:
                    skillInfos = await response.json()
                    skillInfos = skillInfos[0]
                    neededUses = skillInfos["usesToUpgrade"]
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
                        body={
                            "rank": newRank,
                            "uses": "0"
                        }               
                        await ctx.send(f">>> A pericia {skill} subiu para o rank {newRank}")
                    else:
                        body={
                            "uses": uses
                        }
                    async with session.patch(f"{url}/characters/{id}/skills", headers=header, json=body) as e:
                        pass
        else:
            body={
                skill: "F"
            }
            async with session.post(f"{url}/characters/{id}/skills", headers=header, json=body) as resp:
                pass