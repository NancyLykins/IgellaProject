import links from "../config.js"

const screen = document.getElementById("screen")

function createItemForm(){
    let background = document.createElement("div")
    background.setAttribute("class", "modal")
    let modal = document.createElement("div")
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
        </div>
        <div class="formItem labeledInput" id="imageInput">
            <label for="itemImage" id="itemImageLabel">Adicionar imagem do item</label>
            <input type="file" name="image" id="itemImage" accept=".png, .jpeg, .jpg" required>
        </div>
        <textarea name="desc" id="itemDesc"></textarea>
        <button type="submit" id="createItemButton">Criar Item</button>
    </form>
    `
    background.onclick = () =>{
        screen.removeChild(background)
        screen.removeChild(modal)
    }
    modal.setAttribute("id", "m154112")
    modal.appendChild(formContainer)
    screen.append(background, modal)

    let itemType = document.getElementById("itemType")
    itemType.addEventListener("onchange", ()=>{
        let value = itemType.value
        itemType.style.width = "none"
    })
}

export default createItemForm
