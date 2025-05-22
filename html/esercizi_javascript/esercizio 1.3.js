let x = 10;
let y;
y = x;
let z = "Mario";

// lato client

document.getElementById("x").textContent = `x:${x} ` + `type: ` + typeof x;
document.getElementById("y").textContent = `y:${y} ` + `type: ` + typeof y;
document.getElementById("z").textContent = `z:${z} ` + `type: ` + typeof z;

// lato server

console.log(`x:${x} ` + `type: ` + typeof x);
console.log(`y:${y} ` + `type: ` + typeof y);
console.log(`z:${z} ` + `type: ` + typeof z);