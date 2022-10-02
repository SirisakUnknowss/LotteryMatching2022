/***********************************************
    For load Order by API
***********************************************/
let isWorking = false;

window.addEventListener('load', (event) => {
    requestContent()
})

async function clearData() {
    const dataTableBody = document.querySelector("#dataTableBody")
}

async function loadContent(params = "") {
    const response = await fetch(url + params, {
        method: 'GET',
        headers: {'Content-type': 'application/json'},
        cache: 'no-store'
    })
    if (!response.ok){
        isWorking = false
    }
    const jsonObject = await response.json()
    console.log(jsonObject)
    return jsonObject
}

async function requestContent(params) {
    clearData()
    .then( () => loadContent(params))
    .then(jsonObject => display(jsonObject))
}