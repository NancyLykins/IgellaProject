import links from "../config.js";
import loadInventary from "./inventary/loadInventary.js";
import loadStatus from "./loadStatus.js";
const searchResults = document.getElementById("searchResults")
async function loadPlayers(){
    let api = links["api"]
    let response = await fetch(`${api}/characters/names`)
    let data = await response.json()
    searchResults.innerHTML = ""
    for(let i = 0; i<data.length; i++){
        let div = document.createElement("div")
        let name = data[i]["nome"]
        div.innerText = name
        div.onclick = async() => {
            let response = await fetch(`${links["api"]}/characters/${name}`)
            let data = (await response.json())[0]
            loadStatus(data)
            loadInventary(data["id"])
            fetch(`${links["server"]}/server/session.php`, {
                method: "post",
                body: JSON.stringify({
                    "playerId": data["id"] 
                }),
                headers: {
                    "Content-type": "application/json"
                }
            })
        }
        div.setAttribute("class", "palyer")
        searchResults.appendChild(div)     
    }
}

export default loadPlayers