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
    row.appendChild(shopEle)
    row.appendChild(userNameEle)
    row.appendChild(passwordEle)
    row.appendChild(manageEle)
    return row
}

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