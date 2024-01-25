import requests, json

header = {'Content-Type': 'application/json'}
body = {
    "hp": "25",
    "mp": "78",
    "forca": "18"
}
requests.patch(f"http://localhost:5050/characters/663141450564894750", data=json.dumps(body), headers=header)