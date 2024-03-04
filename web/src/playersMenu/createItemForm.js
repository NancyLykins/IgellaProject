import links from "../config.js"

const screen = document.getElementById("screen")

function createItemForm(){
    let background, modal, formContainer, itemType, itemImage
    background = document.createElement("div")
    background.setAttribute("class", "modal")
    modal = document.createElement("div")
    background.onclick = () =>{
        screen.removeChild(background)
        screen.removeChild(modal)
    }
    modal.setAttribute("id", "m154112")
    formContainer = createBase()
    modal.appendChild(formContainer)
    screen.append(background, modal)
    itemImage=document.getElementById("itemImage")
    itemImage.addEventListener("change", ()=>{
        let fileName = itemImage.value
        fileName = fileName.split("\\")[2].split(".")
        let p = document.createElement("p")
        p.innerText = fileName[0]
        document.getElementById("itemImageInfo").innerText = "Image Name:"
        document.getElementById("itemImageLabel").append(p)
    })
    itemType = document.getElementById("itemType")
    itemType.addEventListener("change", ()=>controlOptions())
}

function controlOptions(){
    let value, modal
    value = itemType.value
    modal = document.getElementById("m154112")
    optionsComplement = document.getElementById("optionsComplement")
    optionsComplement.innerHTML = null
    
    switch(value){
        case "item":
            modal.style.height = "35%"
            break
        case "usable":
            modal.style.height = "35%"
            break
        case "equipable":
            modal.style.height = "50%"
            createEquipableOptions(optionsComplement)
            break
    }

}

function createEquipableOptions(optionsComplement){
    let equipableTypes, selectTypes 
    equipableTypes = {
        "null": "Selecione uma opção",
        "armo": "Armadura",
        "hands": "Mão(s)",
        "equipament": "Equipamentos"
    }
    selectTypes = document.createElement("select")
    selectTypes.setAttribute("name", "typeComplement")
    selectTypes.setAttribute("id", "typeComplement")
    selectTypes.setAttribute("class", "optionComplement")
    for(let key in equipableTypes){
        let element = document.createElement("option")
        element.setAttribute("value", key)
        element.innerText = equipableTypes[key]
        selectTypes.appendChild(element)
    }
    selectTypes.addEventListener("change", ()=>{
        let value, typeComplement, bodyPart, handsOptions, baublesSlots
        typeComplement = document.getElementById("typeComplement")
        value = typeComplement.value
        bodyPart = document.getElementById("bodyPart")
        if(bodyPart!=null) optionsComplement.removeChild(bodyPart)
        handsOptions = document.getElementById("handsOptions")
        if(handsOptions != null) optionsComplement.removeChild(handsOptions)
        baublesSlots = document.getElementById("baublesSlots")
        if(baublesSlots != null) optionsComplement.removeChild(baublesSlots)
        switch(value){
            case "armo":
                createArmoOptions(optionsComplement)
                break
            case "hands":
                createHandsOptions(optionsComplement)
                break
            case "equipament":
                createBaublesOptions(optionsComplement)
                break
            case "null": break
        }
    })
    optionsComplement.appendChild(selectTypes)
    
    function createBaublesOptions(optionsComplement){
        let baubles, baublesSlots
        baubles={
            "null": "Selecione uma opção",
            "necklace": "Colar",
            "bra": "Bracelet",
            "ring": "Anel"
        }
        baublesSlots = document.createElement("select")
        baublesSlots.setAttribute("name", "baublesSlots")
        baublesSlots.setAttribute("id", "baublesSlots")
        baublesSlots.setAttribute("class", "optionComplement")
        for(let key in baubles){
            let option = document.createElement("option")
            option.setAttribute("value", key)
            option.innerText = baubles[key]
            baublesSlots.appendChild(option)
        }
        optionsComplement.appendChild(baublesSlots)
        console.log(optionsComplement)
    }

    function createHandsOptions(optionsComplement){
        let handsOptions, hands
        hands={
            "null": "Selecione uma opção",
            "oneH": "Uma mão",
            "twoH": "Duas mãos"
        }
        handsOptions = document.createElement("select")
        handsOptions.setAttribute("name", "handsOptions")
        handsOptions.setAttribute("id", "handsOptions")
        handsOptions.setAttribute("class", "optionComplement")
        for(let key in hands){
            let option = document.createElement("option")
            option.setAttribute("value", key)
            option.innerText = hands[key]
            handsOptions.appendChild(option)
        }
        optionsComplement.appendChild(handsOptions)
    }

    function createArmoOptions(optionsComplement){
        let bodyParts, parts
        parts = {
            "null": "Selecione uma opção",
            "head": "Cabeça",
            "chest": "Tronco",
            "legs": "Pernas",
            "feets": "Pés"
        }
        bodyParts = document.createElement("select")
        bodyParts.setAttribute("name", "bodyPart")
        bodyParts.setAttribute("id", "bodyPart")
        bodyParts.setAttribute("class", "optionComplement")
        for(let key in parts){
            let option = document.createElement("option")
            option.setAttribute("value", key)
            option.innerText = parts[key]
            bodyParts.appendChild(option)
        }
        optionsComplement.append(bodyParts)
    }
}

function createBase(){
    let formContainer = document.createElement("div")
    formContainer.setAttribute("id", "formContainer")
    formContainer.innerHTML = `
    <form action="${links["server"]}/server/processData/item.php" method="post" id="itemForm" enctype="multipart/form-data">
        <div class="formItem labeledInput">
            <label for="itemName">Nome:</label>
            <input type="text" name="name" id="itemName" placeholder="Escreva o nome do item" required>
        </div>
        <div class="formItem labeledInput">
            <label for="itemWeight">Peso:</label>
            <input type="number" name="weight" id="itemWeight" required>
            <select name="unity" id="weightUnity">
                <option value="gram">g</option>
                <option value="quilo">Kg</option>
            </select>
        </div>
        <div class="formItem labeledInput">
            <label for="itemType">Tipo</label>
            <select name="type" id="itemType">
                <option value="item" default>Objeto</option>
                <option value="usable">Consumivel</option>
                <option value="equipable">Equipavel</option>
            </select>
            <div id="optionsComplement"></div>
        </div>
        <div class="formItem labeledInput" id="imageInput">
            <label for="itemImage" id="itemImageLabel">
                <spam id="itemImageInfo">Adicionar imagem do item</spam>
                <input type="file" name="image" id="itemImage" accept=".png, .jpeg, .jpg" required>
            </label>
        </div>
        <textarea name="desc" id="itemDesc"></textarea>
        <button type="submit" id="createItemButton">Criar Item</button>
    </form>
    `
    return formContainer
}

export default createItemForm