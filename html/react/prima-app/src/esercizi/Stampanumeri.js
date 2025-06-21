import React from 'react'

function Stampanumeri() {

    const numeri = [];
    for (let i = 1; i <= 10; i++) {
        numeri.push(
            <li key = {i}>
                {i}
            </li>
        );
    }

  return (
    <>
        <h2>Numeri da 1 a 10</h2>
        <ul>
            {numeri}
        </ul>
    </>
  );
}

export default Stampanumeri;