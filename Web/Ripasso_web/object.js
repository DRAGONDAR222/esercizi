// Creazione oggetto
const persona = {
  nome: "Dario",
  età: 25,
  saluta: function() {
    console.log("Ciao, sono " + this.nome);
  }
};

// Accesso ai valori
console.log(persona.nome); // "Dario"
console.log(persona["età"]); // 25

// Aggiungere proprietà
persona.città = "Milano";

// Cancellare proprietà
delete persona.età;

// Chiamare metodo
persona.saluta(); // "Ciao, sono Dario"
