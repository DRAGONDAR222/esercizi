import React from 'react';
import { useState } from 'react';
import { posts } from '../dati/dati_esercizio_slide5';

const EsercizioSlide5 = () => {

    const [show, setShow] = useState(true);
    const [color, setColor] = useState(true);

    return (

        <div className="container">
            <div className="row">
                <div className="col- justify-text-center">
                    <button type="button" class="btn btn-primary" onClick={() => setShow(!show)}>{show ? "Nascondi" : "Visualizza"}</button>
                    <button type="button" class="btn btn-primary" onClick={() => setColor(!color)}>{color ? "Nero" : "Bianco"}</button>
                </div>
            </div>
                <br></br>

            <div className="container">
                <div className="row">
                    {
                        show &&
                        posts.map((i, index) => (
                            <div className="col-md-3 mb-4" key={index}>
                                <div className="card h-100">
                                    <ul className="list-group list-group-flush" >
                                        <li className="list-group-item" style={{ backgroundColor: color ? "black" : "white", color: color ? "white" : "black" }}>ID: {i.id}</li>
                                        <li className="list-group-item" style={{ backgroundColor: color ? "black" : "white", color: color ? "white" : "black" }}>Titolo: {i.titolo}</li>
                                        <li className="list-group-item" style={{ backgroundColor: color ? "black" : "white", color: color ? "white" : "black" }}>Descrizione: {i.descrizione}</li>
                                    </ul>
                                </div>
                            </div>
                        ))}
                </div>
            </div>
        </div>
    );
};


export default EsercizioSlide5;
