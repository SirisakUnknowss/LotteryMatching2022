/***********************************************
    For load Order by API
***********************************************/
let isWorking = false;

window.addEventListener('load', (event) => {
    requestContent()
})

async function clearRobot() {
}

async function loadContent(params = "") {
    const response = await fetch(url + params, {
        method: 'GET',
        headers: {'Content-type': 'application/json'},
        cache: 'no-store'
    })
    if (!response.ok){
        //throw new Error('Error Occured:' + response.statusText)
        // orderBlock = document.querySelector(".robotList > .noresults")
        // orderBlock.innerHTML = "NO RESULTS" 
        // document.getElementById('totalNum').innerHTML = "0"
        isWorking = false
    }
    const jsonObject = await response.json()
    console.log(jsonObject)
    return jsonObject
}

async function requestContent(params) {
    clearRobot()
    .then( () => loadContent(params))
    // .then(jsonObject => console.log(jsonObject))
    .then(jsonObject => display(jsonObject))
    // .catch(reason => console.log(reason.toString()))
}