// Esercizio 6: Rendering Condizionale
// Obiettivo: Mostrare o nascondere elementi della UI in base a una condizione. Componente
// da creare: MessaggioSegreto.js
// Istruzioni:
// 1.​ Crea il componente MessaggioSegreto.js.
// 2.​ Usa useState per creare uno stato booleano mostra, inizializzato a false.
// 3.​ Crea un bottone che al onClick inverte il valore di mostra.
// 4.​ Usa l'operatore ternario per cambiare il testo del bottone.
// 5.​ Usa l'operatore && per mostrare un paragrafo con un "messaggio segreto" solo se
// mostra è true.
// 6.​ Importa e usa <MessaggioSegreto /> in App.js.


import React, { useState } from 'react';

const MessaggioSegreto = () => {

    const [mostra, setMostra] = useState(false);

    const segreto = 'Questo è un messaggio segreto'


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

            <button onClick={() => setMostra(!mostra)}>{mostra ? 'Nascondi' : 'Mostra'}</button>
            <p>{mostra && segreto}</p>
        </div>
    )
}

export default MessaggioSegreto