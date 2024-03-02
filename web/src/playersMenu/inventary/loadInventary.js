import links from "../../config.js"
import editInventaryItem from "./editInventaryItem.js"
const inventarySlots = document.getElementById("inventarySlots")

async function loadInventary(id){
    let response = await fetch(`${links["api"]}/characters/${id}/inventary`)
    let data = await response.json()
    inventarySlots.innerHTML = ""
    for(let i=0; i < data.length; i++){
        let div, item, itemImg, itemQuant, itemEdit
        div = document.createElement("div")
        div.setAttribute("class", "slot")
        div.setAttribute("title", data[i]["name"].charAt(0).toUpperCase() + data[i]["name"].slice(1))
        item = document.createElement("div")
        item.setAttribute("class", "itemDiv")
        itemImg = document.createElement("img")
        itemImg.setAttribute("src", `${links["api"]}/${data[i]["imagePath"]}`)
        itemQuant = document.createElement("span")
        itemQuant.innerText = data[i]["quant"]
        itemImg.setAttribute("class", "item itemImg")
        itemImg.setAttribute("draggable", "True")
        itemImg.setAttribute("id", data[i]["name"].replace(/ /g, "_"))
        itemImg.setAttribute("draggable", "false")
        itemQuant.setAttribute("class", "itemQuant")
        item.append(itemImg, itemQuant)
        itemEdit = document.createElement("span")
        itemEdit.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
            <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
            <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/>
        </svg>`
        itemEdit.onclick = () =>{
            editInventaryItem(data[i])
        }
        div.append(item, itemEdit)
        inventarySlots.appendChild(div)
    }
}

export default loadInventary


