import links from "../../config.js"
import loadInventary from "./loadInventary.js"

export default function editInventaryItem(data){
    const inventary = document.getElementById("inventary")
    let editMenu, imgDiv, infosDiv, img, itemName, itemId, itemQuantContainer, itemQuantLabel, itemQuant, itemSave
    if(!document.getElementById("itemMenu")){
        editMenu = document.createElement("div")
        editMenu.setAttribute("id", "itemMenu")
    }else{
        editMenu = document.getElementById("itemMenu")
        while(editMenu.firstChild){
            editMenu.removeChild(editMenu.firstChild)
        }
    }
    imgDiv = document.createElement("div")
    infosDiv = document.createElement("div")
    infosDiv.setAttribute("id", "itemDiv")
    img = document.createElement("img")
    img.setAttribute("src", `${links["api"]}/${data["imagePath"]}`)
    img.setAttribute("draggable", "false")
    imgDiv.appendChild(img)
    itemName = document.createElement("p")
    itemId = document.createElement("p")
    itemName.innerText = data["name"]
    itemName.setAttribute("id", "itemName")
    
    itemQuant = document.createElement("input")
    itemQuantLabel = document.createElement("p")
    itemQuant.value = data["quant"]
    itemQuant.setAttribute("id", "quant")
    itemQuant.setAttribute("type", "number")
    itemQuantLabel.innerText = "Quantidade:"
    
    itemQuantContainer = document.createElement("div")
    itemQuantContainer.append(itemQuantLabel, itemQuant)
    
    itemSave = document.createElement("button")
    itemSave.innerText = "Salvar alteração"
    itemSave.setAttribute("id", "saveItem")
    infosDiv.append(itemName, itemQuantContainer, itemSave)
    editMenu.append(imgDiv, infosDiv)
    inventary.appendChild(editMenu)

    itemSave.onclick = save
    itemQuant.addEventListener("keypress", (e)=>{
        if(e.key == "Enter")save()
    })
    function save(){
        let quant = document.getElementById("quant").value
        if(!parseInt(quant)){
            console.log(quant)
            if(quant == "0"){
                fetch(`${links["api"]}/processData/inventary/deleteItem.php`,{
                    method: "post",
                    body: JSON.stringify({
                        "itemId": data["rowId"]
                    }),
                    headers:{
                        "Content-type": "application/json"
                    }
                })
            }
            console.error(`${quant} is NaN\nThis value is'n valid for the quant`)
            return 0
        }
        fetch(`${links["server"]}/server/processData/editItemQuant.php`, {
            method: "post",
            body: JSON.stringify({
                "itemId": data["rowId"],
                "quant": quant,
            }),
            headers: {
                "Content-type": "application/json"
            },
        })
        .then((response)=>{
            if(response.status == 200){
                loadInventary(data["characterId"])
            }
        })
    }
}