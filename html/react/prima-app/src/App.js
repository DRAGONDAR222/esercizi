import './App.css';
import Componente1 from './Componente1';
import Clock from './Clock';
import Tabellina from './esercizi/Tabellina';
import Stampanumeri from './esercizi/Stampanumeri';
import Stampanumeri2 from './esercizi/Stampanumeri2';
import Persona from './esercizi/Persona';
import Contatore from './esercizi/Contatore';
import ProfiloUtente from './esercizi/ProfiloUtente';


// esercizio ProfiloUtente
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

// divisione in 3 per booststrap
function dividiInGruppi(array) {
  const gruppi = [];
  for (i = 0; i < array.length; i += 3) {
    gruppi.push(array.slice(i, i + 3)); // i si aggiorna ad ogni ciclo (3,6...)
  }                 //da(incluso) a (escluso)
  return gruppi;
}


function App() {
  let nome ="Dario"
  return (
    <div className="App">
      <br></br>
      <Componente1>{nome}</Componente1>
      <h1>Prima app di {nome}</h1>
      <Clock timezone='0' country='Italia'></Clock>
      <Clock timezone='-6' country='USA'></Clock>
      <Clock timezone='7' country='Japan'></Clock>
      <br></br>
      <Persona persona={{ nome: "Marco", cognome: "Togni", eta: 31 }}/>
      <Tabellina numero={5} />
      <Stampanumeri/>
      <Stampanumeri2/>
      <br></br>
      <Contatore/>
      <br></br>

      <div className="container mt-4">
        {dividiInGruppi(utenti, 3).map((gruppo, idx) => (
          <div className="row mb-4" key={idx}>
            {gruppo.map((utente) => (
              <div className="col-md-4" key={utente.id}>
                <ProfiloUtente utente={utente} />
              </div>
            ))}
          </div>
        ))}
      </div>
      
      </div>

  );
}

export default App;
