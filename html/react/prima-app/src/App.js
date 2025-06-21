import './App.css';
import Componente1 from './Componente1';
import Clock from './Clock';
import Tabellina from './esercizi/Tabellina';
import Stampanumeri from './esercizi/Stampanumeri';
import Stampanumeri2 from './esercizi/Stampanumeri2';
import Persona from './esercizi/Persona';




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
      <Persona persona={{ nome: "Marco", cognome: "Rossi", eta: 31 }} />
      <Tabellina numero={5} />
      <Stampanumeri/>
      <Stampanumeri2/>
      
      </div>

  );
}

export default App;
