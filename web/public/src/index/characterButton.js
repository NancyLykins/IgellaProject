import links from "../config.js"
import loadCharacter from "./loadCharacter.js"
export default async function characterButton(name){
    let response = await fetch(`${links["api"]}/character/${name}`)
    let data = await response.json()
    loadCharacter(data)
}