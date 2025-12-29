// Selezione elemento per ID

document.getElementById("id"); // Restituisce l'elemento con l'ID specificato



// Manipolazione del contenuto

element.textContent = "Testo"; 
    // Inserisce solo testo, ignorando HTML
element.innerHTML = "<strong>HTML</strong>"; 
    // Inserisce contenuto HTML interpretato
element.value = "nuovo valore"; 
    // Cambia il valore di un input (es. <input>)



// Aggiungere un event listener

element.addEventListener("click", function(e) {
  console.log("cliccato"); // Funzione eseguita al click dell'elemento
});

// Eventi comuni:
// "click"       -> Azione di click dell'utente
// "input"       -> Cambiamento del valore di un input mentre si digita
// "submit"      -> Invio di un form
// "change"      -> Cambiamento di un input dopo la perdita di focus
// "keydown"     -> Tasto premuto
// "keyup"       -> Tasto rilasciato
// "mouseover"   -> Passaggio del mouse sopra un elemento



// Gestione dei form

form.addEventListener("submit", function(e) {
  e.preventDefault(); // Impedisce l’invio predefinito della pagina
  console.log(form.elements["nomeCampo"].value); // Legge il valore del campo con name="nomeCampo"
});
