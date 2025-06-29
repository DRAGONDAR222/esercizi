function Utente(id,nome,cognome,eta,professione,email){
    this.id = id;
    this.nome = nome;
    this.cognome = cognome;
    this.eta = eta;
    this.professione = professione;
    this.email = email;
}


// Creazione di 3 utenti
const utente1 = new Utente(1, "Luca", "Rossi", 30, "Ingegnere", "luca.rossi@email.com");
const utente2 = new Utente(2, "Maria", "Bianchi", 25, "Designer", "maria.bianchi@email.com");
const utente3 = new Utente(3, "Giovanni", "Verdi", 40, "Medico", "giovanni.verdi@email.com");

// inserimento nell'array
let  utenti = [utente1, utente2, utente3];

