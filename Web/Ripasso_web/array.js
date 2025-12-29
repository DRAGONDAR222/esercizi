// Creazione array
const numeri = [1, 2, 3, 4, 5];

// Accesso agli elementi
console.log(numeri[0]); // 1

// Rimuovere elementi
numeri.pop(2);    // 3

// Iterare
numeri.forEach(num => console.log(num));

// Trasformare con map
const doppi = numeri.map(num => num * 2);
console.log(doppi); // [2,4,6,8,...]
