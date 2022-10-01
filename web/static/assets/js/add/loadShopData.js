const shopSelect = document.querySelector("#shopSelect")
const shopAddManySelect = document.querySelector("#shopAddManySelect")
window.addEventListener('load', (event) => {
    requestContentShop()
})

async function clearData() {
}

async function loadContentShop(params = "") {
    const response = await fetch(urlshop + params, {
        method: 'GET',
        headers: {'Content-type': 'application/json'},
        cache: 'no-store'
    })
    if (!response.ok){
        isWorking = false
    }
    const jsonObject = await response.json()
    return jsonObject
}

async function requestContentShop(params) {
    clearData()
    .then( () => loadContentShop(params))
    .then(jsonObject => displayShop(jsonObject))
}

async function displayShop(jsonObject)
{
    let result = jsonObject.result
    if (result.length > 0)
    {
        for (let index=0; index < result.length; index++)
        {
            optionEle = document.createElement("option")
            optionEle.value = result[index].id
            optionEle.innerHTML = result[index].name
            shopSelect.appendChild(optionEle)

            optionAddManyEle = document.createElement("option")
            optionAddManyEle.value = result[index].id
            optionAddManyEle.innerHTML = result[index].name
            shopAddManySelect.appendChild(optionAddManyEle)
        }
    }
}