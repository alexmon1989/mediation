const casesCountForm = document.querySelector("#form-cases-count")

casesCountForm.onsubmit = function (event) {
    event.preventDefault()
    event.stopPropagation()
    if (casesCountForm.checkValidity()) {
        const mediatorPk = JSON.parse(document.getElementById('mediator-pk').textContent)
        const searchParams = new URLSearchParams({
            date_from: document.querySelector("#form-cases-count #date-from").value,
            date_to: document.querySelector("#form-cases-count #date-to").value,
        })
        document.getElementById('period-count').innerHTML = '<i class="text-muted">завантаження даних...</i>'
        fetch('/cases/cases-count/' + mediatorPk + '/?' + searchParams)
            .then((response) => {
                return response.json()
            })
            .then((data) => {
                if (data.result === 'success') {
                    document.getElementById('period-count').innerHTML = data.count
                } else {
                    document.getElementById('period-count').innerHTML = '<span class="text-danger">помилка: ' + data.msg + '</span>'
                }
            });
    }
};
