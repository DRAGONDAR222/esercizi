import { useEffect, useState } from "react";


const urlUser = "https://jsonplaceholder.typicode.com/users";
const UserCrud = () => {
    const [users, setUsers] = useState([]);


    const getUsers = () => {
        fetch(urlUser)
            .then((response) => response.json())
            .then((ris) => setUsers(ris));
    };
    useEffect(() => {
        getUsers();
    }, []);


    const deleteUser = (id) => {
        const newUsers = users.filter((u) => u.id !== id);
        if (window.confirm("Sei sicuro di voler cancellare questo utente?")) {
            setUsers(newUsers);
        }
    };


    return (
        <>
            <div className="container">
                <h1>USER CRUD</h1>


                <div className="card shado-sm mb-4">
                    <div className="card-body">
                        <h2 className="card-title mb-4">Gestione utente</h2>
                        <form >

                            <div className="row g-3 mb-3">
                                <div className="col-md-6">
                                    <label htmlFor="nome" className="form-label fw-bold">Nome *</label>
                                    <input
                                        type="text"
                                        id="nome"
                                        name="nome"
                                        className="form-control"

                                        required
                                    />
                                </div>
                                <div className="col-md-6">
                                    <label htmlFor="cognome" className="form-label fw-bold">Cognome *</label>
                                    <input
                                        type="text"
                                        id="cognome"
                                        name="cognome"
                                        className="form-control"

                                        required
                                    />
                                </div>
                            </div>
                            <div className="row g-3 mb-4">
                                <div className="col-md-6">
                                    <label htmlFor="telefono" className="form-label fw-bold">Telefono</label>
                                    <input
                                        type="tel"
                                        id="telefono"
                                        name="telefono"
                                        className="form-control"

                                    />
                                </div>
                                <div className="col-md-6">
                                    <label htmlFor="email" className="form-label fw-bold">Email *</label>
                                    <input
                                        type="email"
                                        id="email"
                                        name="email"
                                        className="form-control"

                                        required
                                    />
                                </div>
                            </div>


                            <div className="d-flex gap-2">
                                <button type="submit" className="btn btn-primary">
                                    Salva dati
                                </button>


                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </>
    );
};


export default UserCrud;
