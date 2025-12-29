// Creare un elemento

const div = document.createElement("div"); // Crea un nuovo <div>



// Riempire l’elemento

div.textContent = "Ciao!"; // Inserisce solo testo
div.innerHTML = "<strong>Ciao!</strong>"; // Inserisce HTML interpretato



// Aggiungere stile

div.style.color = "red"; // Cambia colore del testo



// Aggiungere l’elemento al DOM

document.body.appendChild(div); // Inserisce il <div> nella pagina



// Creare un elemento e aggiungerlo dentro un contenitore

const p = document.createElement("p"); // Nuovo <p>
p.textContent = "Paragrafo di esempio"; // Contenuto
contenitore.appendChild(p); // Aggiunto dentro #contenitore


//-------------------------------------------------------------


// Esempio completo

const frutti = ["Mela", "Banana", "Pera"];
const ul = document.createElement("ul");

// Uso .map con arrow function e const per ogni li
frutti.map(frutto => {
  const li = document.createElement("li"); // Creo un <li>
  li.textContent = frutto;                  // Inserisco il testo
  ul.appendChild(li);                        // Aggiungo alla lista
});

document.body.appendChild(ul);               // Inserisco la lista nella pagina
