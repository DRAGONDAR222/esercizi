import logo from './logo.svg';
import './App.css';
import Componente1 from './Componente1';

let nome ="Dario"

function App() {
  return (
    <div className="App">
      <Componente1></Componente1>
     <h1>Prima App React di {nome}</h1>
     <h2>
      {
        new Date().toLocaleDateString()+ " " + new Date().toLocaleDateString()
      }
     </h2>
    </div>
  );
}

export default App;
