// Array
const arr1 = [1, 2];
const arr2 = [3, 4];
const arrUnito = [...arr1, ...arr2]; // [1,2,3,4]

// Copia array
const copiaArr = [...arr1]; // evita di modificare l'originale

// Oggetti
const obj1 = {a: 1, b: 2};
const obj2 = {...obj1, c: 3}; // {a:1, b:2, c:3}