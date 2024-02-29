import links from "../config.js";

const inventary = document.getElementById("inventarySlots")

document.addEventListener("dragstart", (e)=>{
    if(e.target.classList[0] == "item"){
        e.dataTransfer.setData("Text", e.target.id)
    }
})
document.addEventListener("dragover", (e)=>{
    e.preventDefault();
})
document.addEventListener("drop", (e)=>{
    e.preventDefault();
    if(e.target.id == "inventarySlots"){
        let itemId, item, quant, name, id
        let itens = []
        for(let i=1; i < inventary.childNodes.length; i++){
            itens.push(inventary.childNodes[i].title.toLowerCase().replace(/ /g, "_"))
        }
        if(!itens.includes("moeda") && inventary.childNodes[0].data != "\n        "){
            if(inventary.childNodes[0].title.toLowerCase() == "moeda"){
                itens.push("moeda")
            }
        }
        itemId = e.dataTransfer.getData("Text")
        if(itens.includes(itemId.toLowerCase())){
            item = document.querySelectorAll(`#${itemId}`)
            item = item[item.length-1]
            name = item.parentElement.parentElement.title
            quant = parseInt(item.nextElementSibling.innerText)+1
            item.nextElementSibling.innerText = quant
        } else{
            item = document.getElementById(itemId).parentElement.parentElement.cloneNode(true)
            name = item.title
            quant = 1
            item.lastChild.lastChild.innerText = quant
            item.lastChild.firstChild.draggable = "false"
            e.target.appendChild(item)
        }
        fetch(`${links["server"]}/server/processData/giveItens.php`,{
            method: "post",
            body: JSON.stringify({
                "item": {
                    "name": name.toLowerCase().replace(/ /g, "+"),
                    "quant": quant
                }
            }),
            headers: {
                "Content-type": "application/json"
            }
        })
    }
})