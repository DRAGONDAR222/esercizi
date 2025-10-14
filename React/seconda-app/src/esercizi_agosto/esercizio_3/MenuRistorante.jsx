// Esercizio 3: Renderizzare Liste con .map()
// Obiettivo: Visualizzare dinamicamente una lista di elementi partendo da un array.
// Componente da creare: MenuRistorante.js
// Istruzioni:
// 1.​ Crea un file piatti.js in src ed esporta un array di oggetti. Ogni oggetto deve
// avere id, nome e prezzo.
// 2.​ Crea il componente MenuRistorante.js e importa l'array di piatti.
// 3.​ Usa il metodo .map() sull'array per renderizzare una lista <ul> di piatti.
// 4.​ Ogni <li> deve contenere il nome e il prezzo del piatto e deve avere un attributo
// key univoco (usa piatto.id).
// 5.​ Importa e usa <MenuRistorante /> in App.js.


import React from 'react'
import piatti from './piatti'

const MenuRistorante = () => {
    return (
        <ul>
            {
                piatti.map(piatto => (
                    <li key={piatto.id}>
                        <b>Nome: </b>{piatto.nome}
                        <br/>
                        <b>Prezzo: </b>{piatto.prezzo}
                    </li>
                ))
            }
        </ul>
    )
}

export default MenuRistorante