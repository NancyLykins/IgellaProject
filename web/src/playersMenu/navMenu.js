import loadPlayers from "./loadPlayers.js"
import loadItens from "./loadItens.js"
const playerButton = document.getElementById("playerButton")
const itenButton = document.getElementById("itenButton")


function main(){
    playerButton.onclick = loadPlayers
    itenButton.onclick = loadItens
}

main()