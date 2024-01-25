import os
async def setup_hook(client):
    for root, dirs, files in os.walk("./"):
        for file in files:
            if not root.endswith("__pycache__"):
                path = os.path.join(root, file)[:-3].replace('/', '.')
                print(f"Loading {path}")
                await client.load_extension(path)