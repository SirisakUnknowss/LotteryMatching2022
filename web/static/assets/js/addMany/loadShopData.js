const shopAddManySelect = document.querySelector("#shopAddManySelect")
const shopSearchSelect = document.querySelector("#shopSearchSelect")
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
    .then(() => {
        
    var value = shopSearchSelect.options[shopSearchSelect.selectedIndex].value
    requestContent("?shop="+value)
    })
}

async function displayShop(jsonObject)
{
    let result = jsonObject.result
    if (result.length > 0)
    {
        for (let index=0; index < result.length; index++)
        {
            optionAddManyEle = document.createElement("option")
            optionAddManyEle.value = result[index].id
            optionAddManyEle.innerHTML = result[index].name
            if (String(result[index].id) == String(idShop))
            {
                optionAddManyEle.setAttribute("selected", "selected")
            }
            shopAddManySelect.appendChild(optionAddManyEle)

            optionSearchEle = document.createElement("option")
            optionSearchEle.value = result[index].id
            optionSearchEle.innerHTML = result[index].name
            if (String(result[index].id) == String(idShop)) { optionSearchEle.setAttribute("selected", "selected") }
            shopSearchSelect.appendChild(optionSearchEle)
        }
    }
}