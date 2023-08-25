
const input_length = document.querySelector("#input_length")
const confirmAddManyNumber = document.querySelector("#confirmAddManyNumber")
const formSendNumber = document.querySelector("#formSendNumber")
const formSendManyNumber = document.querySelector("#formSendManyNumber")
const addOneNumber = document.querySelector("#addOneNumber")
// const shopAddSelect = document.querySelector("#shopSelect")
// const shopAddManySelect = document.querySelector("#shopAddManySelect")

function inputLength()
{
    if (input_length.value.length < 6) input_length.focus()
}

confirmAddManyNumber.addEventListener('click', event => {
    waiting()
    shopSelect.value = shopSelect.options[shopSelect.selectedIndex].value
    shopAddManySelect.value = shopAddManySelect.options[shopAddManySelect.selectedIndex].value
    event.preventDefault()
    formSendManyNumber.submit()
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

function waiting() {
	$('*').css('cursor','wait');
	$('*').css('pointer-events','none');
}

function stopWaiting() {
	$('*').css('cursor','default');
	$('*').css('pointer-events','auto');
}