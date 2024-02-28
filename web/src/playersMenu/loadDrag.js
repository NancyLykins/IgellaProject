const inventary = document.getElementById("inventarySlots")

document.addEventListener("dragstart", (e)=>{
    if(e.target.classList[0] == "item"){
        e.dataTransfer.setData("Text", e.target.id)
        console.log(e.target)
    }
})
document.addEventListener("dragover", (e)=>{
    e.preventDefault();
});

document.addEventListener("drop", (e)=>{
    e.preventDefault();
    if(e.target.id == "inventarySlots"){
        let itens = []
        for(let i=1; i < inventary.childNodes.length; i++){
            itens.push(inventary.childNodes[i].title.toLowerCase().replace(/ /g, "_"))
        }
        if(!itens.includes("moeda") && inventary.childNodes.length > 1){
            if(inventary.childNodes[0].title.toLowerCase() == "moeda"){
                itens.push("moeda")
            }
        }
        let itemId = e.dataTransfer.getData("Text")
        console.log(itemId)
        console.log(itens)
        if(itens.includes(itemId.toLowerCase())){
            let item = document.querySelectorAll(`#${itemId}`)
            item = item[item.length-1]
            item.nextElementSibling.innerText = parseInt(item.nextElementSibling.innerText)+1
        } else{
            let item = document.getElementById(itemId).parentElement.parentElement.cloneNode(true)
            item.lastChild.lastChild.innerText = 1
            item.lastChild.firstChild.draggable = "false"
            e.target.appendChild(item)
        }
    }
})

