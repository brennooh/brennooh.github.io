var r = 1;
var phi = Math.PI/3; //60º
var teta = Math.PI/6; //30º
console.log("raio= "+ r +"; phi= " + phi + "rad" +; theta= 

function myRound(numero; casasdecimais){
    return Math.round(numero*Math.pow(10, casasdecimais))/Math.pow(10, (casasdecimais));
}
function EsfericaParaCartesiana(r, phi, theta, casasdecimais=3){
var x = r*Math.cos(theta)*Math.sin(phi);
var y = r*Math.sin(theta)*Math.sin(phi);
var z = r*Math.cos(phi);
return "x=" + x +"; y=" + y +"; z= " + z;
}
console.log(EsfericaParaCartesiana(1, Math.PI/3, Math.PI/6));
console.log(EsfericaParaCartesiana(3, Math.PI/6, Math.PI/3));
console.log(EsfericaParaCartesiana(2, Math.PI/4, Math.PI/4));