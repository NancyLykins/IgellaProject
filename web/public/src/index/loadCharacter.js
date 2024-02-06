export default function loadCharacter(data){
    data = data[0]
    document.getElementById("characterInfos").style.display = "flex"
    document.getElementById("characterName").innerText = data["nome"]
    hpBar(data["hp"], data["maxHP"])
    mpBar(data["mp"], data["maxMp"])
    xpBar(data["xpAtual"], data["xpNextLvl"])
    document.getElementById("level").innerText = `Level: ${data['level']}`
    document.getElementById("power").innerText = `Magia: ${data['magia']}`
    document.getElementById("age").innerText = `Idade: ${data['idade']}`
    document.getElementById("gender").innerText = `Gênero: ${data['genero'][0]}`
    document.getElementById("class").innerText = `Classe: ${data['classe']}`
    document.getElementById("race").innerText = `Raça: ${data['raca']}`
    document.getElementById("agi").innerText = `${data['agilidade']} + ${data['agilidadeBuff']}`
    document.getElementById("for").innerText = `${data['forca']} + ${data['forcaBuff']}`
    document.getElementById("int").innerText = `${data['inteligencia']} + ${data['inteligenciaBuff']}`
    document.getElementById("pre").innerText = `${data['presenca']} + ${data['presencaBuff']}`
    document.getElementById("vig").innerText = `${data['vigor']} + ${data['vigorBuff']}`
    document.getElementById("armo").innerText = data['armo']
    document.getElementById("points").innerText = data['pontosRestantes']
}


function hpBar(hp, totalHp){
    document.getElementById("hpValues").innerText = `${hp}/${totalHp}`
    document.getElementById("restHp").style.width = `${calculatePorcent(hp, totalHp)}%`
}
function mpBar(mp, totalMp){
    document.getElementById("manaValues").innerText = `${mp}/${totalMp}`
    document.getElementById("restMana").style.width = `${calculatePorcent(mp, totalMp)}%`

}
function xpBar(xp, totalXp){
    document.getElementById("xpValues").innerText = `${xp}/${totalXp}`
    document.getElementById("totalXp").style.width = `${calculatePorcent(xp, totalXp)}%`

}
function calculatePorcent(fill, full){
    return 100*fill/full
}