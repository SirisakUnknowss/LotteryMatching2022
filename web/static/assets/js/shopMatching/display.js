
async function display(jsonObject)
{
    let result = jsonObject.result
    const dataTableBody = document.querySelector("#dataTableBody")
    if (result.length > 0)
    {
        for (let number=0; number < result.length; number++)
        {
            // table = createCol(result[number])
            // console.log(table)
            // dataTableBody.appendChild(table)
            parentClassSelector = "#divCardData"
            table = createTable()
            tbodyEle = document.createElement('tbody')
            row = createCol(result[number])
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
    cardEle.className = "card mb-3 container w-50"
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
    shopEle = document.createElement(tag)
    shopEle.innerHTML = result.name
    numberEle = createNumberMatchingRow(result.number)
    row.appendChild(shopEle)
    row.appendChild(numberEle)
    return row
}

function createRow()
{
    tag = "tr"
    className = "odd"
    nameEle = createHTMLEle(tag, className)
    return nameEle
}


function createNumberMatchingRow(result)
{
    tag = "td"
    numberEle = createHTMLEle(tag, className)
    numberEle.className = "text-right"
    for (let number=0; number < result.length; number++)
    {
        tagP = document.createElement('p')
        tagP.className = "mb-1"
        tagP.innerHTML = result[number]
        numberEle.appendChild(tagP)
    }
    return numberEle
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