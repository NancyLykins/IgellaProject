import loadPlayers from "./loadPlayers.js"
const playerButton = document.getElementById("playerButton")
const itenButton = document.getElementById("itenButton")


function main(){
    playerButton.onclick = loadPlayers
}

main()