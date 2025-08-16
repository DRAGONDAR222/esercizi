// Questa funzione controlla se i campi del modulo sono validi
function validaForm() {
    // Ottieni i valori dei campi
    const cognome = document.forms["mioForm"]["cognome"].value;            // creo delle "costanti" recuperando i "valori" dal file html 
    const nome = document.forms["mioForm"]["nome"].value;
    const matricola = document.forms["mioForm"]["matricola"].value;
    const regione = document.forms["mioForm"]["regione"].value;
    const email = document.forms["mioForm"]["email"].value;
    const telefono = document.forms["mioForm"]["telefono"].value;

    // Controllo: il cognome non deve essere vuoto
    if (cognome.trim() === "") {                                          // il .trim() esclude tutti gli spazi digitati
        alert("Il campo 'Cognome' è obbligatorio.");                      // il alert() avvisa l'utente
        return false; // Impedisce l'invio del modulo
    }

    // Controllo: il nome non deve essere vuoto
    if (nome.trim() === "") {
        alert("Il campo 'Nome' è obbligatorio.");
        return false;
    }

    // Controllo: la matricola deve essere un numero
    if (isNaN(matricola) || matricola.trim() === "") {                   // isNaN() verifica se un valore è "Not-a-Number"
        alert("Il campo 'Matricola' deve contenere un numero.");
        return false;
    }

    // Controllo: deve essere selezionata una regione
    if (regione === "") {
        alert("Seleziona una regione.");
        return false;
    }

    // Controllo: email o telefono devono essere riempiti
    if (email.trim() === "" && telefono.trim() === "") {                // && corrisponde ad: "and"
        alert("Inserisci almeno un contatto: 'Email' o 'Telefono'.");
        return false;
    }

    // Se tutti i controlli passano, il modulo viene inviato
    return true;
}
