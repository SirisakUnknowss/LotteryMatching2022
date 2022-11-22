
async function readNumber(idNumber) {
    let data = new FormData();
    data.append('idNumber', idNumber)
    data.append('page', pageName)
    // var raw = JSON.stringify({
    //     "idNumber": idNumber,
    //     "page": pageName
    //     });
        
    data.append('csrfmiddlewaretoken', $('#csrf-helper input[name="csrfmiddlewaretoken"]').attr('value'))
    var requestOptions = {
    method: 'POST',
    headers: {'Content-type': 'multipart/form-data'},
    body: data,
    cache: 'no-store',
    credentials: 'same-origin',
    };
    
    fetch(readNumberUrl, requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
}