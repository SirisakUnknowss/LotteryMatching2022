
const input_length = document.querySelector("#input_length")
const confirmAddNumber = document.querySelector("#confirmAddNumber")
const formSendNumber = document.querySelector("#formSendNumber")
const addOneNumber = document.querySelector("#addOneNumber")

function inputLength()
{
    if (input_length.value.length < 6) input_length.focus()
}

confirmAddNumber.addEventListener('click', event => {
    shopSelect.value = shopSelect.options[shopSelect.selectedIndex].value
    if (input_length.value.length != 6) return alert("กรุณากรอกหมายเลขให้ครบถ้วน!")
    else { checkTypeNumber() }
    event.preventDefault()
    
})

function checkTypeNumber()
{
    if (isNaN(input_length.value))
    {
        input_length.focus()
        return alert("กรุณากรอกหมายเลขให้ถูกต้อง!")
    }
    else
    {
        addOneNumber.value = (input_length.value)
        formSendNumber.submit()
    }
}