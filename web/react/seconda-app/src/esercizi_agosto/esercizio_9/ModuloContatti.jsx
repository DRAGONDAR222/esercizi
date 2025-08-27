// Esercizio 9: Gestire Form Complessi con un Singolo Stato
// Obiettivo: Gestire un form con più campi usando un singolo oggetto per lo stato.
// Componente da creare: ModuloContatti.js
// Istruzioni:
// 1. Crea il componente ModuloContatti.js.
// 2. Usa useState per inizializzare uno stato come oggetto: { nome: '', email:
// '', messaggio: '' };.
// 3. Crea un form con tre input (nome, email) e una textarea (messaggio). Aggiungi
// a ognuno l'attributo name corrispondente.
// 4. Crea una sola funzione handleChange per tutti i campi. All'interno, usa lo spread
// operator per aggiornare solo il campo modificato.
// 5. Gestisci l'evento onSubmit del form per stampare l'oggetto datiForm in console.
// 6. Importa e usa <ModuloContatti /> in App.js.


import React, { useState } from 'react'

const ModuloContatti = () => {

    const [dati, setDati] = useState({ nome: '', email: '', messaggio: '' });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setDati((prevDati) => ({
            ...prevDati,
            [name]: value,
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Dati del form:', dati);
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
        >
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Nome:</label>
                    <input
                        type="text"
                        name="nome"
                        value={dati.nome}
                        onChange={handleChange}
                    />
                </div>
                <div>
                    <label>Email:</label>
                    <input
                        type="text"
                        name="email"
                        value={dati.email}
                        onChange={handleChange}
                    />
                </div>
                <div>
                    <label>Messaggio:</label>
                    <textarea
                        name="messaggio"
                        value={dati.messaggio}
                        onChange={handleChange}
                    />
                </div>
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}

export default ModuloContatti