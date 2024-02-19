import links from "../../config.js";
const searchResults = document.getElementById("searchResults")
async function loadItens(){
    let item
    let response = await fetch(`${links["api"]}/itens`)
    let data = await response.json()
    searchResults.innerHTML = ""
    let itensContainer = document.createElement("div")
    itensContainer.setAttribute("class", "slotsContainer")
    for(let i=0; i < data.length; i++){
        item = data[i]
        let div = document.createElement("div")
        div.setAttribute("class", "slot")
        let itemDiv = document.createElement("div")
        let itemImg = document.createElement("img")
        //itemImg.setAttribute("data", data[i]["img "])
        let itemQuant = document.createElement("span")
        itemQuant.innerText = item["rowId"]
        itemImg.setAttribute("class", "itemImg")
        itemQuant.setAttribute("class", "itemQuant")
        itemDiv.append(itemImg, itemQuant)
        div.appendChild(itemDiv)
        itensContainer.append(div)
    }
    searchResults.appendChild(itensContainer)
}

export default loadItens