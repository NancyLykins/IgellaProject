import links from "../config.js";
import createItemForm from "./createItemForm.js";
const searchResults = document.getElementById("searchResults")
async function loadItens(){
    let item, div, itemDiv, itemImg, itemQuant
    let response = await fetch(`${links["api"]}/itens`)
    let data = await response.json()
    searchResults.innerHTML = ""
    let itensContainer = document.createElement("div")
    itensContainer.setAttribute("class", "slotsContainer")
    for(let i=0; i < data.length; i++){
        item = data[i]
        console.log(item)
        div = document.createElement("div")
        div.setAttribute("class", "slot")
        div.setAttribute("title", item["name"].charAt(0).toUpperCase() + item["name"].slice(1))
        itemDiv = document.createElement("div")
        itemImg = document.createElement("img")
        itemImg.setAttribute("src", `${links["api"]}/${item["imagePath"]}`)
        itemImg.setAttribute("draggable", "True")
        itemImg.style.cursor = "Move"
        itemQuant = document.createElement("span")
        itemQuant.innerText = item["rowId"]
        itemImg.setAttribute("class", "itemImg")
        itemQuant.setAttribute("class", "itemQuant")
        itemDiv.setAttribute("class", "itemDiv")
        itemDiv.append(itemImg, itemQuant)
        div.appendChild(itemDiv)
        itensContainer.appendChild(div)
    }
    div = document.createElement("div")
    div.setAttribute("class", "slot")
    div.innerHTML = `
    <svg style="cursor: pointer;" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="#fff" class="bi bi-plus-lg" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M8 2a.5.5 0 0 1 .5.5v5h5a.5.5 0 0 1 0 1h-5v5a.5.5 0 0 1-1 0v-5h-5a.5.5 0 0 1 0-1h5v-5A.5.5 0 0 1 8 2"/>
    </svg>
    `
    div.onclick = () =>{
        createItemForm()
    }
    itensContainer.appendChild(div)
    searchResults.appendChild(itensContainer)
}

export default loadItens