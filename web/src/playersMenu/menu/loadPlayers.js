import links from "../../config.js";
const searchResults = document.getElementById("searchResults")
async function loadPlayers(){
    let api = links["api"]
    let data = await fetch(`${api}/characters/names`)
    let result = await data.json()
    for(let i = 0; i<result.length; i++){
        let div = document.createElement("div")
        div.innerText = result[i]["nome"]
        div.setAttribute("class", "palyer")
        searchResults.appendChild(div)     
    }
}

export default loadPlayers