const dataTableHover_previous = document.querySelector("#dataTableHover_previous")
const dataTableHover_next = document.querySelector("#dataTableHover_next")

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