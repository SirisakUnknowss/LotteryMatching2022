
async function readNumber(idNumber) {
    var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value')
    $.ajax({
        type: "POST",
        url: readNumberUrl,
        data: JSON.stringify({
                  "idNumber": idNumber,
                  "page": pageName
                }),
        headers:{"X-CSRFToken": $crf_token,  "Content-Type": "application/json"},
        success: function (newEnd)
        {
            const dataTableBody = document.getElementById("dataTableBody")
            const rowNumber = document.getElementById("row-number" + idNumber)
            dataTableBody.removeChild(rowNumber)
        },
        error: function () {
            alert("can't not read is number")
        }
    })
}