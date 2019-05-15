var pares = [];
function isPar (numero){
    if (numero%2 == 0){
        return true;}
        else {
            return false;
        }
        }

function Q1() {
    console.log('Q1');
    var aux = Number.parseInt (document.getElementById('numeroQ1').value);
    // Segue aqui seu código
    for (let i = 0; i <= aux; i++){
        if (isPar(i)){
            pares.push(i);
        }

    }
    console.log (pares);
    document.getElementById('RQ1').innerHTML = pares;
}

var primos = [];
function isPrimo (numero){
    if (numero === 2) {return  true;}
    else if (numero < 2 || numero %2 === 0) {
        return false;}
        for (let i = 3; i <= Math.sqrt(numero); i+= 2){
            if (numero % i === 0) {return false;}
        }
        return true;
    }



function Q2() {
    console.log('Q2');
    var aux = Number.parseInt (document.getElementById('numeroQ2').value);
    // Segue aqui seu código
    
}