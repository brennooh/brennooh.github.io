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
var listaStrings = [];
function acrescentaSTR() {
    var aux = document.getElementById('novaString').value;
    listaStrings.push(aux);
    document.getElementById('novaString').value = "";
    document.getElementById('auxQ3').innerHTML = listaStrings;
    console.log (listaStrings);
}
function Q3() {
    console.log('Q3');
    for (let i = 0; i < listaStrings.length; i++){
        listaStrings[i] = listaStrings [i]. toUpperCase ();
    }
    console.log(listaStrings);
    document.getElementById('RQ3').innerHTML = listaStrings;
    }
function QuickSort_ (X, IniVet, FimVet){
    var i = IniVet
    var j = FimVet;
    var pivo = X (Math.floor((IniVet+FimVet)/2))
    var aux;
    
    while (i <= j){
        while (X[i] < pivo){
            i++;
        }
        while (x[i] > pivo){
            j--;
        }
        if (i <= j){
            aux = X[i];
            X[i] = X[j];
            X[j] = aux;
            i <- i++;
            j <- j--;
        }
        }
        if (IniVet < j){
            QuickSort(X, IniVet, j);
        }
        if (i < FimVet){
            QuickSort (X,FimVet,i);
        }
        }
function QuickSort (X){
    var y = Array.from(X);
    QuickSort_(Y, 0, Y.length -1);
    return Y;
}
function Q4() {
    console.log('Q4');
    var aux = document.getElementById('numerosQ4').value;
    var numerosQ4 = aux.split (';');
    var ordenados;
    for (let i = 0; i < numerosQ4.lenght; i++){
        numerosQ4[i] = Number.parseFloat (numerosQ4[i]);
    }
    ordenados = QuickSort(numerosQ4);
    console.log(ordenados);
    }

    // ========================
    function appendMA(){
        var aux = document.getElementById('linhaA').valor;
        for (let i = 0; i < aux.lenght; i++){
            aux[i] = number.parseFloat (aux [i]);
        }
        matrizA.push(aux);
        console.log(matrizA)

    }