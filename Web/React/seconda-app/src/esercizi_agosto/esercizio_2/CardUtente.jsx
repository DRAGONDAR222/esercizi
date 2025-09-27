// Esercizio 2: Componenti Dinamici con le Props
// Obiettivo: Imparare a passare dati a un componente per renderlo riutilizzabile.
// Componente da creare: CardUtente.js
// Istruzioni:
// 1. Crea il file CardUtente.js.
// 2. Modifica il componente affinché accetti props come argomento.
// 3. Il componente deve visualizzare un nome, un'email e un'immagine avatar. Usa
// props.nome, props.email e props.imgUrl per accedere ai dati.
// ○ Esempio di JSX: <h2>{props.nome}</h2> <p>{props.email}</p>
// <img src={props.imgUrl} alt="Avatar utente" />
// 4. In App.js, importa CardUtente e usalo almeno due volte, passando dati diversi
// per ogni card. Puoi usare un'immagine placeholder come
// https://placehold.co/

import React from 'react';

const CardUtente = (props) => (
  <div
    className="
      container
      d-flex
      flex-column
      justify-content-center
      align-items-center
      text-center
    "
  >
    <img
      src={props.imgUrl}
      alt="Avatar"
      width="200"
      height="200"
    />
    <h2>{props.nome}</h2>
    <p>{props.email}</p>
  </div>
);

export default CardUtente;
