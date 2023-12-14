function getPrice() {
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;

    const obj = {
        "method": "get-price",
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })
    .then(function(resp) {
        return resp.json();
    })
    .then(function(data) {
        document.querySelector('#price').innerHTML = `Цена напитка: ${data.result} руб`;
        document.querySelector('#pay').style.display = '';
    })
}

let savedCardNum

function pay() {
    const card_num = document.querySelector('[name=card_num]').value;
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;
    const cvv = document.querySelector('[name=cvv]').value;

    savedCardNum = card_num;

    const obj = {
        "method": "pay",
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar,
            card_num: card_num,
            cvv: cvv
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })
    .then(function(resp) {
        return resp.json();
    })
    .then(function(data) {
        if (data.error) {
            document.querySelector('#error_message').innerHTML = data.error;
        } 
        else {
            document.querySelector('#error_message').innerHTML = '';
            document.querySelector('#lol').innerHTML = `${data.result}`;
            document.querySelector('#pay').style.display = 'none';
            document.querySelector('#price').style.display = 'none';
            document.querySelector('#pay_back').style.display = '';
        }
    })


}


function refund() {
    const card_num =  savedCardNum;
    const drink = document.querySelector('[name=drink]:checked').value;
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;

    
    const obj = {
        "method": "refund",
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar,
            card_num: card_num,
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })

    .then(function(resp) {
        return resp.json();
    })

    .then(function(data) {
            document.querySelector('#lol').innerHTML = `${data.result}`;
            document.querySelector('#back').style.display = ''
    })

}
