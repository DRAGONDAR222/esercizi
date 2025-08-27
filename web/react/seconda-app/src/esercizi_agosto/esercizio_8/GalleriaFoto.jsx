// Esercizio 8: Caricare Dati da un Server (Data Fetching)Obiettivo: Usare useEffect per caricare dati da un'API esterna e gestire gli stati di
// caricamento ed errore. Componente da creare: GalleriaFoto.js
// Istruzioni:
// 1.​ Crea il componente GalleriaFoto.js.
// 2.​ Definisci tre stati: foto (array vuoto), staCaricando (true), errore (null).
// 3.​ Usa useEffect (con dipendenza []) per fare una fetch all'URL:
// https://jsonplaceholder.typicode.com/photos?_limit=10.
// 4.​ Dentro useEffect, usa una funzione async/await e un blocco try/catch.
// 5.​ Nel try, se la richiesta va a buon fine, popola lo stato foto e imposta
// staCaricando a false.
// 6.​ Nel catch, imposta lo stato errore con il messaggio di errore e staCaricando a
// false.
// 7.​ Nel JSX, gestisci i tre stati: mostra un messaggio di caricamento, un messaggio di
// errore, o la galleria di foto (mappando l'array foto e mostrando le immagini).


import React from 'react'
import { useState } from 'react'
import { useEffect } from 'react';

const GalleriaFoto = () => {

    const url = 'https://jsonplaceholder.typicode.com/photos?_limit=10';

    const [foto, setFoto] = useState([]);
    const [staCaricando, setStaCaricando] = useState(true);
    const [errore, setErrore] = useState(null);

    const getData = async () => {
        setErrore(false);
        setStaCaricando(true);
        try {
            const response = await axios.get(url)
            setFoto(response.data)
        } catch (err) {
            console.log(err)
            setErrore(true)
        }
        setStaCaricando(false);
    };

    useEffect(() => {
        getData();
    }, [])

    if (staCaricando) {
        return <h3>Caricamento...</h3>
    };

    if (errore) {
        return <h2>Si è verificato un'errore</h2>
    };

    return (
        <div
            className="
                container
                d-flex
                justify-content-center
                flex-column
                align-items-center
        "
        ><ul>
                {
                    foto.map((f) => {
                        return (
                            <li key={f.id}>
                                <div>
                                    <img src={f.url} alt="" />
                                    <h5>{f.title}</h5>
                                </div>
                            </li>
                        )
                    })
                }
        </ul></div>
    )
}

export default GalleriaFoto