import React from 'react';

function Tabellina({ numero }) {
  if (numero < 1 || numero > 10) {
    return <p>Il numero deve essere compreso tra 1 e 10.</p>;
  }

  const righe = [];
  for (let i = 1; i <= 10; i++) {
    righe.push(
      <li key={i}>
        {numero} × {i} = {numero * i}
      </li>
    );
  }

  return (
    <div>
      <h2>Tabellina del {numero}</h2>
      <ul>
        {righe}
      </ul>
    </div>
  );
}

export default Tabellina;
