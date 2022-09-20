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
        // const scriptDatabase = document.querySelector("#scriptDatabase")
        // scriptDatabase.src = urlDataTables
        $('#dataTableHover').DataTable();
    }
}

function createCol(result)
{
    row = createRow()
    tag = "td"
    numberEle = document.createElement(tag)
    numberEle.innerHTML = result.numberLottery
    shopEle = document.createElement(tag)
    nameShop = ""
    if (result.user.shop == null) nameShop = "ไม่มีข้อมูล"
    else nameShop = result.user.shop.name
    shopEle.innerHTML =nameShop
    userAddEle = document.createElement(tag)
    userAddEle.innerHTML = result.user.username
    statusEle = document.createElement(tag)
    imageRead = imgUnRead
    isRead = ""
    if (isRead)
    {
        imageRead = imgRead
        isRead = "อ่านแล้ว"
    }
    else isRead = "ยังไม่อ่าน"
    
    imgEle = document.createElement('img')
    pEle = document.createElement('span')
    imgEle.className = "mx-2"
    imgEle.src = imageRead
    pEle.innerHTML = isRead
    statusEle.appendChild(imgEle)
    statusEle.appendChild(pEle)
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
    parentEle = document.querySelector(parentClass)
    parentEle.appendChild(ele)
}