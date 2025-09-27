// Esercizio 5: Gestire Input Utente (Controlled Components)
// Obiettivo: Creare un campo di input il cui valore è controllato dallo stato di React.
// Componente da creare: CampoRicerca.js
// Istruzioni:
// 1.​ Crea il componente CampoRicerca.js.
// 2.​ Usa useState per creare uno stato testoRicerca, inizializzato a ''.
// 3.​ Crea un <input type="text" /> e collega il suo value allo stato
// {testoRicerca}.4.​ Gestisci l'evento onChange per aggiornare lo stato con il valore dell'input
// (e.target.value).
// 5.​ Sotto l'input, aggiungi un paragrafo che mostra in tempo reale cosa sta scrivendo
// l'utente: <p>Stai cercando: {testoRicerca}</p>.
// 6.​ Importa e usa <CampoRicerca /> in App.js.


import React, { useState } from 'react';

const CampoRicerca = () => {
    const [testoRicerca, setTestoRicerca] = useState('');

    const handleChange = (e) => {
        setTestoRicerca(e.target.value);
    };

    return (
        <div
            className="
                container
                d-flex
                justify-content-center
                flex-column
                align-items-center
        "
        >
            <input
                type="text"
                value={testoRicerca}
                onChange={handleChange}
                placeholder="Scrivi Testo"
            />
            <p>Stai cercando: {testoRicerca}</p>
        </div>
    );
};

export default CampoRicerca;
