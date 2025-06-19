import './App.css';
import Componente1 from './Componente1';
import Clock from './Clock';
import Tabellina from './Tabellina';

let nome ="Dario"

function App() {
  return (
    <div className="App">
      <Componente1></Componente1>
     <h1>Prima App React di {nome}</h1>
     <h2>
      <Clock></Clock>
     </h2>
     <Clock timezone ="0" country = "Italia">qualcosa</Clock>
     <Tabellina></Tabellina>
    </div>
  );
}

export default App;
