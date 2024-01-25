import os
from client import CLIENT

async def load():
    print("Starting to load cogs")
    for root, dirs, files in os.walk("cogs"):
        for file in files:
            if not root.endswith("__pycache__"):
                path = os.path.join(root, file)[:-3].replace("/", ".")
                print(f"Loading {path}")
                await CLIENT.load_extension(path)
    print("All cogs was loaded")