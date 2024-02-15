import link from "../config.js"
import characterButton from "./characterButton.js"
const characterList = document.getElementById("charactersList")

let response = await fetch(link["api"]+"/characters/names")
let data = await response.json()
for(let i = 0; i < data.length; i++){
    let listElement = document.createElement("li")
    let button = document.createElement("button")
    let name = data[i]["nome"]
    button.onclick = async() => {await characterButton(name)}
    button.innerText = name
    button.setAttribute("class", "characterName")
    listElement.appendChild(button)
    characterList.appendChild(listElement)
}