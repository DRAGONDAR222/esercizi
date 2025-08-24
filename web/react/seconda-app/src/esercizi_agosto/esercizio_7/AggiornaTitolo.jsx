// Esercizio 7: Effetti Collaterali con useEffect
// Obiettivo: Usare useEffect per eseguire un'azione (un "effetto collaterale") in risposta a
// un cambiamento di stato. Componente da creare: AggiornaTitolo.js
// Istruzioni:
// 1.​ Crea il componente AggiornaTitolo.js.
// 2.​ Crea un campo di input controllato (come nell'Esercizio 5) con una variabile di stato
// chiamata nome.
// 3.​ Importa l'hook useEffect da React.
// 4.​ Aggiungi un useEffect che si attivi ogni volta che il valore di nome cambia. Per
// farlo, dovrai usare l'array delle dipendenze: useEffect(() => { ... },
// [nome]);.
// 5.​ All'interno della funzione useEffect, aggiorna il titolo della scheda del browser. Se
// il campo nome è vuoto, il titolo sarà "Benvenuto!", altrimenti document.title =
// \Ciao, ${nome}!`;`.
// 6.​ Quando il componente viene montato, il titolo dovrebbe essere "Benvenuto!".
// Appena l'utente inizia a scrivere, il titolo della pagina si aggiornerà in tempo reale.
// 7.​ Importa e usa <AggiornaTitolo /> in App.js.


import React, { useState, useEffect } from 'react';

const AggiornaTitolo = () => {
    const [nome, setNome] = useState('');

    useEffect(() => {
        nome ? document.title = `Ciao, ${nome}!`: document.title = 'Benvenuto!';
    }, [nome]);

    const gestisciCambio = (e) => {
        setNome(e.target.value);
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
                value={nome}
                onChange={gestisciCambio}
                placeholder="Scrivi Titolo"
            />
        </div>
    );
};

export default AggiornaTitolo;
