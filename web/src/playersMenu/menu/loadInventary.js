import links from "../../config.js"
const inventarySlots = document.getElementById("inventarySlots")

async function loadInventary(id){
    let response = await fetch(`${links["api"]}/characters/${id}/inventary`)
    let data = await response.json()
    inventarySlots.innerHTML = ""
    for(let i=0; i < data.length; i++){
        let div = document.createElement("div")
        div.setAttribute("class", "slot")
        let item = document.createElement("div")
        let itemImg = document.createElement("img")
        //itemImg.setAttribute("data", data[i]["img "])
        let itemQuant = document.createElement("span")
        itemQuant.innerText = data[i]["quant"]
        itemImg.setAttribute("class", "itemImg")
        itemQuant.setAttribute("class", "itemQuant")
        item.append(itemImg, itemQuant)
        div.appendChild(item)
        inventarySlots.appendChild(div)
    }
}

export default loadInventary


