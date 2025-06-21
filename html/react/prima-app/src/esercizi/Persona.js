import React from 'react';

function Persona({ persona }) {
  return (
    <>
      <p><strong>Nome:</strong> {persona.nome}</p>
      <p><strong>Cognome:</strong> {persona.cognome}</p>
      <p><strong>Età:</strong> {persona.eta}</p>
    </>
  );
}

export default Persona;
