async function display(jsonObject)
{
    let result = jsonObject.result
    if (result.length > 0)
    {
        for (let number=1; number < result.length + 1; number++)
        {
            index = number - 1
            parentClassSelector = "#dataTableBody"
            row = createCol(result[index])
            appendHTMLEle(row, parentClassSelector)
            // createColBlock(result[index], parentClassSelector)
        }
    }
}

function createCol(result)
{
    row = createRow()
    tag = "td"
    numberEle = document.createElement(tag)
    numberEle.innerHTML = result.numberLottery
    shopEle = document.createElement(tag)
    shopEle.innerHTML = result.user.shop.name
    userAddEle = document.createElement(tag)
    userAddEle.innerHTML = result.user.username
    statusEle = document.createElement(tag)
    statusEle.innerHTML = result.isRead
    manageEle = document.createElement(tag)
    row.appendChild(numberEle)
    row.appendChild(shopEle)
    row.appendChild(userAddEle)
    row.appendChild(statusEle)
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
    console.log("ele ---- " + ele)
    console.log("parentClass ---- " + parentClass)
    parentEle = document.querySelector(parentClass)
    
    console.log("parentEle ---- " + parentEle)
    parentEle.appendChild(ele)
}