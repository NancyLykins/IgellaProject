import requests, os
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")
header = {'Content-type': 'application/json'}
async def calculateSkillUses(ctx, skill):
    id = ctx.author.id
    response = requests.get(f"{url}/characters/{id}/skills/{skill}")
    data = response.json()[0]
    if data != []:
        rank = data["rank"]
        uses = data["uses"] + 1
        if(rank != "S"):
            response = requests.get(f"{url}/skills/rank/{rank}")
            skillInfos = response.json()[0] 
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
            requests.patch(f"{url}/characters/{id}/skills", headers=header, json=body)
    else:
        body={
            skill: "F"
        }
        requests.post(f"{url}/characters/{id}/skills", headers=header, json=body)