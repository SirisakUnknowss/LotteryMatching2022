
const input_length1 = document.querySelector("#input_length1")
const input_length2 = document.querySelector("#input_length2")
const input_length3 = document.querySelector("#input_length3")
const input_length4 = document.querySelector("#input_length4")
const input_length5 = document.querySelector("#input_length5")
const input_length6 = document.querySelector("#input_length6")

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