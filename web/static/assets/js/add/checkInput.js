
const input_length1 = document.querySelector("#input_length1")
const input_length2 = document.querySelector("#input_length2")
const input_length3 = document.querySelector("#input_length3")
const input_length4 = document.querySelector("#input_length4")
const input_length5 = document.querySelector("#input_length5")
const input_length6 = document.querySelector("#input_length6")
const confirmAddNumber = document.querySelector("#confirmAddNumber")
const formSendNumber = document.querySelector("#formSendNumber")
const number = document.querySelector("#number")

function inputLength1()
{
    if (input_length1.value.length > 0) input_length2.focus()
    else input_length1.focus()
}
function inputLength2()
{
    if (input_length2.value.length > 0) input_length3.focus()
    else input_length1.focus()
}
function inputLength3()
{
    if (input_length3.value.length > 0) input_length4.focus()
    else input_length2.focus()
}
function inputLength4()
{
    if (input_length4.value.length > 0) input_length5.focus()
    else input_length3.focus()
}
function inputLength5()
{
    if (input_length5.value.length > 0) input_length6.focus()
    else input_length4.focus()
}
function inputLength6()
{
    if (input_length6.value.length > 0) input_length6.focus()
    else input_length5.focus()
}

confirmAddNumber.addEventListener('click', event => {
    if (input_length1.value.length == 0 || input_length2.value.length == 0 ||
        input_length3.value.length == 0 || input_length4.value.length == 0 ||
        input_length5.value.length == 0 || input_length6.value.length == 0) return alert("กรุณากรอกหมายเลขให้ครบถ้วน!")
    else { checkTypeNumber() }
    event.preventDefault()
    
})

function checkTypeNumber()
{
    if (isNaN(input_length1.value))
    {
        input_length1.focus()
        return alert("กรุณากรอกหมายเลขให้ถูกต้อง!")
    }
    else if (isNaN(input_length2.value))
    {
        input_length2.focus()
        return alert("กรุณากรอกหมายเลขให้ถูกต้อง!")
    }
    else if (isNaN(input_length3.value))
    {
        input_length3.focus()
        return alert("กรุณากรอกหมายเลขให้ถูกต้อง!")
    }
    else if (isNaN(input_length4.value))
    {
        input_length4.focus()
        return alert("กรุณากรอกหมายเลขให้ถูกต้อง!")
    }
    else if (isNaN(input_length5.value))
    {
        input_length5.focus()
        return alert("กรุณากรอกหมายเลขให้ถูกต้อง!")
    }
    else if (isNaN(input_length6.value))
    {
        input_length6.focus()
        return alert("กรุณากรอกหมายเลขให้ถูกต้อง!")
    }
    else
    {
        number.value = (input_length1.value + input_length2.value + input_length3.value + input_length4.value + input_length5.value + input_length6.value)
        formSendNumber.submit()
    }
}