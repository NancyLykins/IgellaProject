import links from "../config.js"
const inventarySlots = document.getElementById("inventarySlots")

async function loadInventary(id){
    let response = await fetch(`${links["api"]}/characters/${id}/inventary`)
    let data = await response.json()
    inventarySlots.innerHTML = ""
    for(let i=0; i < data.length; i++){
        let div = document.createElement("div")
        div.setAttribute("class", "slot")
        div.setAttribute("title", data[i]["name"].charAt(0).toUpperCase() + data[i]["name"].slice(1))
        let item = document.createElement("div")
        item.setAttribute("class", "itemDiv")
        let itemImg = document.createElement("img")
        itemImg.setAttribute("src", `${links["api"]}/${data[i]["imagePath"]}`)
        let itemQuant = document.createElement("span")
        itemQuant.innerText = data[i]["quant"]
        itemImg.setAttribute("class", "itemImg")
        itemQuant.setAttribute("class", "itemQuant")
        itemQuant.style.zIndex = "5"
        item.append(itemImg, itemQuant)
        div.appendChild(item)
        inventarySlots.appendChild(div)
    }
}

export default loadInventary


