import React from 'react'

function Stampanumeri() {

    const numeri = [];
    for (let i = 0; i <= 10; i++) {
        numeri.push(
            <li>
                {i}
            </li>
        );
    }

  return (
    <div>
        <h2>Numeri</h2>
        <ul>
            {numeri}
        </ul>
    </div>
  );
}

export default Stampanumeri;