import aiohttp, os
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("API_URL")
header = {'Content-type': 'application/json'}
async def checkCharacterLevel(id, xp):
    body = {
        "xpAtual": f"+{xp}"
    }
    async with aiohttp.ClientSession() as session:
        await session.patch(f"{url}/characters/{id}", json=body, headers=header)
    
