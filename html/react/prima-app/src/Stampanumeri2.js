import React from 'react'

function Stampanumeri2() {

    const numeri = [];
    for (let i = 0; i <= 20; i+= 2) {
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

export default Stampanumeri2;