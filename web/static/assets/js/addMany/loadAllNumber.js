/***********************************************
    For load Order by API
***********************************************/
let isWorking = false;

async function clearData() {
    const dataTableBody = document.querySelector("#dataTableBody")
    while (dataTableBody.hasChildNodes()) {
        dataTableBody.removeChild(dataTableBody.firstChild)
    }
}

async function loadContent(url="") {
    const response = await fetch(url, {
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

async function requestContent(url="") {
    clearData()
    .then( () => loadContent(url))
    .then(jsonObject => display(jsonObject))
}