import React, { useState, useEffect } from 'react';
import axios from 'axios';

const GalleriaFoto = () => {
    const url = 'https://jsonplaceholder.typicode.com/photos?_limit=10';

    const [foto, setFoto] = useState([]);
    const [staCaricando, setStaCaricando] = useState(true);
    const [errore, setErrore] = useState(null); // inizializzato a null

    const getData = async () => {
        setErrore(null); // reset prima del try
        setStaCaricando(true);
        try {
            const response = await axios.get(url);
            setFoto(response.data);
        } catch (err) {
            console.log(err);
            setErrore(err.message); // salvo il messaggio di errore
        }
        setStaCaricando(false);
    };

    useEffect(() => {
        getData();
    }, []);

    if (staCaricando) {
        return <h3>Caricamento...</h3>;
    }

    if (errore) {
        return <h2>Si è verificato un errore: {errore}</h2>;
    }

    return (
        <div className="container d-flex flex-column align-items-center">
            <ul>
                {foto.map((f) => (
                    <li key={f.id}>
                        <div>
                            <img src={f.url} alt="" />
                            <h5>{f.title}</h5>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default GalleriaFoto;
