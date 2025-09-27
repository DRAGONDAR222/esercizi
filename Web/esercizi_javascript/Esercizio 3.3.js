let input = 3661;

let ore = input / (60 * 60);
let oreIntere = parseInt(ore);
input -= (60 * 60) * oreIntere;

let minuti = input / 60;
let minutiInteri = parseInt(minuti);
input -= 60 * minutiInteri;

let secondi = input;

document.getElementById("output").textContent = `Output:${oreIntere} ore, ` + `${minutiInteri} minuti e ` + `${secondi} secondi`

