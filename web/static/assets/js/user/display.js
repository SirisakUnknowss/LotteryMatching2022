async function display(jsonObject)
{
    let result = jsonObject.result
    if (result.length > 0)
    {
        for (let number=1; number < result.length + 1; number++)
        {
            index = number - 1
            parentClassSelector = "#divCardData"
            table = createTable()
            tbodyEle = document.createElement('tbody')
            row = createCol(result[index])
            tbodyEle.appendChild(row)
            table.appendChild(tbodyEle)
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

function createTable()
{
    tag = "table"
    tableEle = document.createElement(tag)
    tableEle.className = "table align-items-center table-flush"
    return tableEle
}

function createCol(result)
{
    row = createRow()
    tag = "td"
    nameEle = document.createElement(tag)
    nameEle.className = "col-2"
    nameEle.innerHTML = result.name
    userNameEle = document.createElement(tag)
    userNameEle.className = "col-3"
    userNameEle.innerHTML = result.username
    passwordAccountEle = document.createElement(tag)
    passwordAccountEle.className = "col-4 text-center"
    inputPassword = document.createElement("INPUT")
    inputPassword.setAttribute("type", "password")
    inputPassword.className = "form-control form-login w-75 d-inline mr-3"
    inputPassword.disabled = true
    inputPassword.value = result.password
    hidePasswordEle = onclickHidePassword(result, inputPassword)
    passwordAccountEle.appendChild(inputPassword)
    passwordAccountEle.appendChild(hidePasswordEle)
    manageEle = document.createElement(tag)
    createDeleteButton(manageEle, result)
    // createAddUserButton(manageEle, result)
    row.appendChild(nameEle)
    row.appendChild(userNameEle)
    row.appendChild(passwordAccountEle)
    row.appendChild(manageEle)
    return row
}

function onclickHidePassword(result, inputPassword)
{
    hidePasswordEle = document.createElement("i")
    hidePasswordEle.className = "fa fa-eye"
    hidePasswordEle.addEventListener('click', event => {
        if (inputPassword.type == "password")
        {
            // hidePasswordEle.className = "fa fa-eye-slash"
            inputPassword.setAttribute("type", "text")
        }
        else
        {
            // hidePasswordEle.className = "fa fa-eye"
            inputPassword.setAttribute("type", "password")
        }
    })
    return hidePasswordEle
}

function createDeleteButton(manageEle, result)
{
    manageEle.className = "text-right col-3"
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
    onclickUserPopup(a, result)
}

function onclickDelete(button, result)
{
    button.addEventListener('click', event => {
        console.log(result.id)
        const userDelete = document.querySelector("#userDelete")
        const IDUserDelete = document.querySelector("#IDUserDelete")
        IDUserDelete.value = result.id
        userDelete.innerHTML = result.name
    })
}

function onclickUserPopup(button, result)
{
    button.addEventListener('click', event => {
        console.log(result.id)
        const userID = document.querySelector("#userID")
        const userName = document.querySelector("#userName")
        userID.value = result.id
        userName.value = result.name
    })
}

const confirmDeleteUser = document.querySelector("#confirmDeleteUser")
const formDeleteUser = document.querySelector("#formDeleteUser")
confirmDeleteUser.addEventListener('click', event => {
    formDeleteUser.submit()
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