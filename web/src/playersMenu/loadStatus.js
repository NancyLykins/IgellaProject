import links from "../config.js"
import loadPlayers from "./loadPlayers.js"

export default function loadStatus(data){
    let pontosRestantes, agiElement, forElement, intElement, preElement, vigElement, attrElements, attributesLine
    attrElements = ["agilidade", "forca", "inteligencia", "presenca", "vigor"]
    pontosRestantes = data["pontosRestantes"]
    agiElement = document.getElementById("agi")
    forElement = document.getElementById("for")
    intElement = document.getElementById("int")
    preElement = document.getElementById("pre")
    vigElement = document.getElementById("vig")
    hpBar(data["hp"], data["maxHP"])
    mpBar(data["mp"], data["maxMp"])
    xpBar(data["xpAtual"], data["xpNextLvl"])
    document.getElementById("characterName").innerText = data["nome"]
    document.getElementById("level").innerText = `Level: ${data['level']}`
    document.getElementById("power").innerText = `Magia: ${data['magia']}`
    document.getElementById("age").innerText = `Idade: ${data['idade']}`
    document.getElementById("gender").innerText = `Gênero: ${data['genero'][0]}`
    document.getElementById("class").innerText = `Classe: ${data['classe']}`
    document.getElementById("race").innerText = `Raça: ${data['raca']}`
    agiElement.innerText = `${data['agilidade']} + ${data['agilidadeBuff']}`
    forElement.innerText = `${data['forca']} + ${data['forcaBuff']}`
    intElement.innerText = `${data['inteligencia']} + ${data['inteligenciaBuff']}`
    preElement.innerText = `${data['presenca']} + ${data['presencaBuff']}`
    vigElement.innerText = `${data['vigor']} + ${data['vigorBuff']}`
    document.getElementById("armo").innerText = data['armo']
    document.getElementById("points").innerText = pontosRestantes
    document.getElementById("playerId").innerText = `ID: ${data["id"]}`
    document.getElementById("characterImg").setAttribute("src", `${links["api"]}/${data["imgPath"]}`)
    
    attributesLine = document.getElementsByClassName("atributesLine")
    if(pontosRestantes > 0 && attributesLine[0].childElementCount < 2){
        for(let i=0; i < attrElements.length; i++){
            let button, attr
            attr = attrElements[i]
            button = document.createElement("button")
            button.setAttribute("class", "upgradeStatus")
            button.onclick = (e) => {
                upgradeStatus(attr, attrElements)
            }
            button.innerHTML = `
            <svg style="cursor: pointer;" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="#000" class="bi bi-plus-lg" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 2a.5.5 0 0 1 .5.5v5h5a.5.5 0 0 1 0 1h-5v5a.5.5 0 0 1-1 0v-5h-5a.5.5 0 0 1 0-1h5v-5A.5.5 0 0 1 8 2"/>
            </svg>
            `
            document.getElementById(`${attr.substring(0, 3)}Attr`).appendChild(button)
        }
    }
    if(pontosRestantes <= 0 && attributesLine[0].childElementCount >= 2){
        for(let i = 0; i < attributesLine.length; i++){
            attributesLine[i].removeChild(attributesLine[i].lastChild)
        }
    }
}

function upgradeStatus(attr, attrElements){
    fetch(`${links["server"]}/server/processData/updateAttr.php`, {
        method: "post",
        body: JSON.stringify({
            "attr": attr
        }),
        headers: {
            "Content-type": "application/json"
        }
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        return fetch(`${links["api"]}/characters/${data["playerId"]}`)      
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        if(data[0]["pontosRestantes"] < 1){
            for(let i=0; i < attrElements.length; i++){
                let j = attrElements[i]
                let element = document.getElementById(`${j.substring(0, 3)}Attr`)              
                element.removeChild(element.lastChild)
            }
        }
        loadStatus(data[0])
    })
}

function hpBar(hp, totalHp){
    document.getElementById("hpValues").innerText = `${hp}/${totalHp}`
    document.getElementById("restHp").style.width = `${calculatePorcent(hp, totalHp)}%`
}
function mpBar(mp, totalMp){
    document.getElementById("manaValues").innerText = `${mp}/${totalMp}`
    document.getElementById("restMana").style.width = `${calculatePorcent(mp, totalMp)}%`

}
function xpBar(xp, totalXp){
    document.getElementById("xpValues").innerText = `${xp}/${totalXp}`
    document.getElementById("totalXp").style.width = `${calculatePorcent(xp, totalXp)}%`

}
function calculatePorcent(fill, full){
    return 100*fill/full
}