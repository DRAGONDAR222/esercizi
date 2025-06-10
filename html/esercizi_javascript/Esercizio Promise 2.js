function job(data) {
    return new Promise((resolve, reject) => {
        if (isNaN(data)) {
            reject("errore");
        } else if (data % 2 !== 0) {
            setTimeout(() => resolve("dispari"), 1000);
        } else {
            setTimeout(() => resolve("pari"), 2000);
        }
    });
}



// Esempi di utilizzo
job(5).then(console.log).catch(console.log); // Dopo 1 sec -> "dispari"
job(10).then(console.log).catch(console.log); // Dopo 2 sec -> "pari"
job("ciao").then(console.log).catch(console.log); // Istantaneo -> "errore"