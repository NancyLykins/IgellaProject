async function fetchAndDisplay(){
    const response = await fetch('include/nav.html')
    document.getElementById('nav').innerHTML = await response.text()
}
fetchAndDisplay()