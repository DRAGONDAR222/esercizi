import React from 'react'

function ProfiloUtente(props) {

    const handleClick = () => {
        alert(`Dettagli utente:\n\nID: ${id}\nNome: ${nome} ${cognome}\nEtà: ${eta}\nProfessione: ${professione}\nEmail: ${email}`);
    };
    
  return (

         <div className="card h-100">
                <div className="card-header text-center">
                    <h5 className="card-title">{nome} {cognome}</h5>
                </div>
                <div className="card-body text-center">
                    <p>
                        <span className="badge bg-primary">{eta} anni</span>
                    </p>
                    <p>{professione}</p>
                    <p>{email}</p>
                </div>
                <div className="card-footer text-center">
                    <button className="btn btn-sm btn-outline-info" onClick={handleClick}>
                        Mostra dettagli
                    </button>
                </div>
            </div>    
        );
}

export default ProfiloUtente