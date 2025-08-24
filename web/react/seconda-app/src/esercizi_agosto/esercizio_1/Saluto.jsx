// Esercizio 1: Il Tuo Primo Componente Statico
// Obiettivo: Prendere confidenza con la creazione di un componente funzionale e la sua
// visualizzazione. Componente da creare: Saluto.js
// Istruzioni:
// 1. Nella cartella src, crea un nuovo file Saluto.js.
// 2. Scrivi il componente senza usare snippet
// 3. All'interno del div restituito, scrivi un messaggio di benvenuto, ad esempio:
// <h1>Benvenuto nel mio primo componente React!</h1>.
// 4. In App.js, importa il componente Saluto (import Saluto from
// './Saluto';).
// 5. Sostituisci il contenuto di default del return di App con il tuo componente <Saluto
// />.

import React from 'react'

const Saluto = () => {
  return (
    <h1>Benvenuto nel mio primo componente React!</h1>
  )
}

export default Saluto