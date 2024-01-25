const menu = document.getElementById("charactersMenu")
const button = document.getElementById("characterMenuControl")
let colapsed = false

button.onclick = ()=>{
    if(colapsed == false){
        colapsed = true
        menu.style.translate = "0%"
        button.style.rotate = "180deg"
    } else  {
        colapsed = false
        menu.style.translate = "-92%"
        button.style.rotate = "0deg"
    }
}