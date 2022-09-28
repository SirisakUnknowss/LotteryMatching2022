async function display(jsonObject)
{
    let result = jsonObject.result
    if (result.length > 0)
    {
        for (let number=1; number < result.length + 1; number++)
        {
            index = number - 1
            parentClassSelector = "#divCardData"
            table = createTable(result[index])
            card = createCard(table)
            appendHTMLEle(card, parentClassSelector)
        }
    }
}

function createCard(table)
{
    tag = "div"
    cardEle = document.createElement(tag)
    cardEle.className = "card mb-3"
    divTableEle = document.createElement(tag)
    divTableEle.className = "table-responsive"
    divTableEle.appendChild(table)
    cardEle.appendChild(divTableEle)
    return cardEle
}

function createTable(result)
{
    tag = "table"
    tableEle = document.createElement(tag)
    tableEle.className = "table align-items-center table-flush"
    tbodyEle = document.createElement('tbody')
    row = createCol(result)
    tbodyEle.appendChild(row)
    tableEle.appendChild(tbodyEle)
    return tableEle
}

function createCol(result)
{
    row = createRow()
    tag = "td"
    shopEle = document.createElement(tag)
    shopEle.innerHTML = result.name
    userNameEle = document.createElement(tag)
    passwordEle = document.createElement(tag)
    manageEle = document.createElement(tag)
    createDeleteButton(manageEle, result)
    createAddUserButton(manageEle, result)
    row.appendChild(shopEle)
    row.appendChild(userNameEle)
    row.appendChild(passwordEle)
    row.appendChild(manageEle)
    return row
}

function createDeleteButton(manageEle, result)
{
    manageEle.className = "text-right"
    var a = document.createElement("a")
    a.href = "javascript:void(0);"
    a.setAttribute("data-toggle", "modal")
    a.setAttribute("data-target", "#deleteModal")
    a.innerHTML = "ลบข้อมูล"
    a.className = "btn btn-danger mb-1"
    manageEle.appendChild(a)
    onclickDelete(a, result)
}

function createAddUserButton(manageEle, result)
{
    manageEle.className = "text-right"
    var a = document.createElement("a")
    a.href = "javascript:void(0);"
    a.setAttribute("data-toggle", "modal")
    a.setAttribute("data-target", "#addUserModal")
    a.innerHTML = "เพิ่มผู้ใช้งาน"
    a.className = "btn btn-info mx-3 mb-1"
    manageEle.appendChild(a)
    onclickShopPopup(a, result)
}

function onclickDelete(button, result)
{
    button.addEventListener('click', event => {
        console.log(result.id)
        const shopDelete = document.querySelector("#shopDelete")
        const IDShopDelete = document.querySelector("#IDShopDelete")
        IDShopDelete.value = result.id
        shopDelete.innerHTML = result.name
    })
}

function onclickShopPopup(button, result)
{
    button.addEventListener('click', event => {
        console.log(result.id)
        const shopID = document.querySelector("#shopID")
        const shopName = document.querySelector("#shopName")
        shopID.value = result.id
        shopName.value = result.name
    })
}

const confirmDeleteShop = document.querySelector("#confirmDeleteShop")
const formDeleteShop = document.querySelector("#formDeleteShop")
confirmDeleteShop.addEventListener('click', event => {
    formDeleteShop.submit()
})

function createRow()
{
    tag = "tr"
    rowName = "row"
    className = "odd"
    nameEle = createHTMLEle(tag, className)
    nameEle.row = rowName
    return nameEle
}

function createColBlock(name, parentClassSelector)
{
    tag = "div"
    className = "name"
    nameEle = createHTMLEle(tag, className)
    nameEle.innerHTML = name
    appendHTMLEle(nameEle, parentClassSelector)
}

function createHTMLEle(tag, className)
{
    ele = document.createElement(tag)
    ele.className = className
    return ele
}

function appendHTMLEle(ele, parentClass)
{
    parentEle = document.querySelector(parentClass)
    parentEle.appendChild(ele)
}