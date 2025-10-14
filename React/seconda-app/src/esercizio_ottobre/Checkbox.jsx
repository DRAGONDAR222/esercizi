// Esercizio: Checkbox Multiple con
// Counter
// Obiettivo
// Creare un componente React che permetta di selezionare delle skills tramite checkbox, con
// conteggio delle selezioni e controllo del limite massimo.
// Requisiti
// Crea un array precompilato di 10 skills tecnologiche. Ogni skill deve avere:
// ● id (number)
// ● name (string)
// Esempio: JavaScript, React, Vue, Angular, TypeScript, Node.js, PHP, Laravel, WordPress,
// CSS/SASS
// Funzionalità richieste
// 1. Visualizzazione lista
// ○ Mostra tutte le skills come checkbox
// ○ Ogni checkbox deve essere cliccabile
// 2. Gestione selezioni (useState)
// ○ Usa useState per mantenere l'array degli ID delle skills selezionate
// ○ Quando clicchi una checkbox, aggiungi o rimuovi l'ID dall'array
// 3. Counter visivo
// ○ Mostra quante skills sono state selezionate (es: "Selezionate: 3 / 10")
// ○ Il counter deve aggiornarsi in tempo reale
// 4. Controllo limite (useEffect)
// ○ Usa useEffect per monitorare il numero di selezioni
// ○ Se l'utente seleziona più di 5 skills, mostra un alert() di avviso
// ○ L'useEffect deve attivarsi solo quando cambia l'array delle selezioni
// 5. Feedback visivo (opzionale)
// ○ Cambia il colore del counter quando superi le 5 selezioni
// ○ Evidenzia le checkbox selezionate
// 6. Mostra un riepilogo delle skills selezionate sotto la lista
// 7. Aggiungi un bottone "Reset" per deselezionare tutto

import React, { useState, useEffect } from "react";
import skills from "./skills";

const Checkbox = () => {
  const [selectedSkills, setSelectedSkills] = useState([]);

  const handleChange = (e, id) => {
    if (e.target.checked) {
      setSelectedSkills(prev => [...prev, id]);
    } else {
      setSelectedSkills(prev => prev.filter(skillId => skillId !== id));
    }
  };

  useEffect(() => {
    if (selectedSkills.length > 5) {
      alert("Hai selezionato più di 5 skills!");
    }
  }, [selectedSkills]);

  const counterClass =  // class bootstrap personalizzata
    selectedSkills.length > 5 ? "text-danger" : "text-dark";

  const handleReset = () => {
    setSelectedSkills([]); // svuota l’array
    };


  return (
    <div className="container mt-3">
      <h2 className={counterClass}>
        Selezionate: {selectedSkills.length} / {skills.length}
      </h2>

      {skills.map(skill => (
        <div className="form-check" key={skill.id}>
          <input
            className="form-check-input"
            type="checkbox"
            id={`checkbox-${skill.id}`}
            checked={selectedSkills.includes(skill.id)}  // se è presente nello useState lo seleziona
            onChange={(e) => handleChange(e, skill.id)}
          />
          <label className="form-check-label" htmlFor={`checkbox-${skill.id}`}>
            {skill.nome}
          </label>
        </div>
      ))}
       <br />
       <h3>Elenco:</h3>

       <ul>
        {skills.map(skill => {
            if (selectedSkills.includes(skill.id)) {
            return <li key={skill.id}>{skill.nome}</li>;
            } 
            return null; // se non è selezionata, non renderizzo nulla
        })}
    </ul>

    <button className="btn btn-secondary mt-3" onClick={handleReset}>
    Reset
    </button>


    </div>
  );
};

export default Checkbox;
