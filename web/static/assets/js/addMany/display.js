
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

function createCol(result)
{
    row = createRow()
    tag = "td"
    numberEle = document.createElement(tag)
    numberEle.innerHTML = result.numberLottery
    shopEle = document.createElement(tag)
    var nameShop = ""
    if (result.idShop != null && result.idShop.length > 0)
    {
        nameShop = result.idShop
    }
    else
    {
        nameShop = "ไม่มีข้อมูล"
    }
    shopEle.innerHTML =nameShop
    userAddEle = document.createElement(tag)
    userAddEle.innerHTML = result.username
    manageEle = document.createElement(tag)
    createDeleteButton(manageEle, result)
    row.appendChild(numberEle)
    row.appendChild(shopEle)
    row.appendChild(userAddEle)
    row.appendChild(manageEle)
    return row
}

function onSelectSearch()
{
    var value = shopSearchSelect.options[shopSearchSelect.selectedIndex].value
    requestContent(url + "?shop="+value)
}

function onSearchNumber()
{
    var value = shopSearchSelect.options[shopSearchSelect.selectedIndex].value
    var number =  document.querySelector("#searchNumber").value
    requestContent(url + "?shop="+value + "&number="+number)
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