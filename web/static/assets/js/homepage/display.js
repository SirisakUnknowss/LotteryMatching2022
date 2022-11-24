async function display(jsonObject)
{
    let result = jsonObject.result
    if (result.length > 0)
    {
        createPreviousButton(jsonObject.links.previous)
        createNextButton(jsonObject.links.next)
        for (let number=1; number < result.length + 1; number++)
        {
            index = number - 1
            parentClassSelector = "#dataTableBody"
            row = createCol(result[index])
            appendHTMLEle(row, parentClassSelector)
        }
        $('#dataTableHover').DataTable();
    }
}

function onSearchNumber()
{
    var number =  document.querySelector("#searchNumber").value
    requestContent(url + "?number="+number)
}

function createPreviousButton(urlPreviousPage)
{
    while (dataTableHover_previous.hasChildNodes()) {
        dataTableHover_previous.removeChild(dataTableHover_previous.firstChild)
    }
    previousPageEle = document.createElement("button")
    previousPageEle.innerHTML = "ก่อนหน้า"
    previousPageEle.className = "page-link"
    if (urlPreviousPage != null)
    {
        previousPageEle.addEventListener('click', event => {
            clearData()
            requestContent(urlPreviousPage)
        })
        dataTableHover_previous.className = "paginate_button page-item previous"
    }
    else
    {
        dataTableHover_previous.className = "paginate_button page-item previous disabled"
    }
    dataTableHover_previous.appendChild(previousPageEle)
}

function createNextButton(urlNextPage)
{
    while (dataTableHover_next.hasChildNodes()) {
        dataTableHover_next.removeChild(dataTableHover_next.firstChild)
    }
    nextPageEle = document.createElement("button")
    nextPageEle.innerHTML = "ถัดไป"
    nextPageEle.className = "page-link"
    if (urlNextPage != null)
    {
        nextPageEle.addEventListener('click', event => {
            clearData()
            requestContent(urlNextPage)
        })
        dataTableHover_next.className = "paginate_button page-item next"
    }
    else
    {
        dataTableHover_next.className = "paginate_button page-item next disabled"
    }
    dataTableHover_next.appendChild(nextPageEle)
}

function createCol(result)
{
    row = createRow()
    row.id = "row-number" + result.id
    tag = "td"
    numberEle = document.createElement(tag)
    numberEle.innerHTML = result.numberLottery
    shopEle = document.createElement(tag)
    nameShop = getnameShops(result.matching)
    shopEle.innerHTML =nameShop
    userAddEle = document.createElement(tag)
    userAddEle.innerHTML = getuserNames(result.matching)
    statusEle = document.createElement(tag)
    imageRead = imgUnRead
    isRead = ""
    if (result.isRead)
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
    imgEle.addEventListener('click', event => {
        readNumber(result.id)
    })
    statusEle.appendChild(imgEle)
    statusEle.appendChild(pEle)
    row.appendChild(numberEle)
    row.appendChild(shopEle)
    row.appendChild(userAddEle)
    row.appendChild(statusEle)
    return row
}

function getnameShops(numbers)
{
    var nameShop = ""
    for (let i=0; i < numbers.length; i++)
    {
        if (numbers[i].idShop != null && numbers[i].idShop.length > 0) nameShop += numbers[i].idShop + "<br />"
        else nameShop += "ไม่มีข้อมูล<br />"
    }
    return nameShop
}

function getuserNames(usernames)
{
    var usernameList = ""
    for (let i=0; i < usernames.length; i++)
    {
        usernameList += usernames[i].username + "<br />"
    }
    return usernameList
}

function createDeleteButton(manageEle, result)
{
    var a = document.createElement("a")
    a.href = "javascript:void(0);"
    a.setAttribute("data-toggle", "modal")
    a.setAttribute("data-target", "#deleteModal")
    a.innerHTML = "ลบข้อมูล"
    a.className = "btn btn-danger mb-1"
    manageEle.appendChild(a)
    onclickDelete(a, result)
}

function onclickDelete(button, result)
{
    button.addEventListener('click', event => {
        const numberDelete = document.querySelector("#numberDelete")
        const IDNumberDelete = document.querySelector("#IDNumberDelete")
        IDNumberDelete.value = result.id
        numberDelete.innerHTML = result.numberLottery
    })
}

const confirmDeleteNumber = document.querySelector("#confirmDeleteNumber")
const formDeleteNumber = document.querySelector("#formDeleteNumber")
confirmDeleteNumber.addEventListener('click', event => {
    formDeleteNumber.submit()
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