import React from 'react';

function Stampanumeri2() {

  const numeri = [];
  for (let i = 0; i <= 20; i += 2) {
    numeri.push(i);
  }

  return (
    <>
      <h2>Numeri da 0 a 20</h2>
      {numeri.map((i, index) => (
        <span key={index}>
          {i}{index !== numeri.length - 1 ? ' - ' : ''}
        </span>
      ))}
    </>
  );
}

export default Stampanumeri2;
