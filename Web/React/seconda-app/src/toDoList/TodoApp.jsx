// Obiettivo: Creare un'applicazione To-Do List completa che interagisce con un backend
// fittizio (json-server) per caricare, aggiungere, eliminare e aggiornare le attività, rendendo
// i dati persistenti.
// Preparazione (se nonavete configurato l’ambiente in aula):
// 1. Installa json-server: Se non l'hai già fatto, apri il terminale e digita: npm install
// -g json-server.
// 2. Crea il database: Nella cartella principale del tuo progetto React, crea un file
// chiamato db.json.
// Popola il database: Incolla questo contenuto in db.json:
// {
// "tasks": [
// { "id": 1, "text": "Imparare le basi di React", "completed": true },
// { "id": 2, "text": "Fare questo esercizio", "completed": false }
// ]
// }
// 3.
// 4. Avvia il server: Dal terminale, nella cartella del progetto, esegui: json-server
// --watch db.json --port 3001. Lascia questo terminale aperto. Ora hai un'API
// REST funzionante all'indirizzo http://localhost:3001/tasks.
// Componenti da creare: TodoApp.js (genitore), TodoForm.js, TodoList.js,
// TodoItem.js.

// 1. TodoApp.js (Componente Principale):
// ○ Qui vivrà lo stato principale: const [tasks, setTasks] =
// useState([]);. Aggiungi anche stati per loading ed error.
// ○ Usa useEffect con dipendenza [] per fare una fetch (GET) all'avvio e
// caricare i task da http://localhost:3001/tasks, aggiornando lo stato
// tasks.
// ○ Crea una funzione async handleAddTask: deve fare una richiesta POST a
// json-server per aggiungere un nuovo task. Dopo il successo, ricarica la
// lista dei task per mostrare quello nuovo.
// ○ Crea una funzione async handleDeleteTask: deve fare una richiesta
// DELETE (/tasks/id) per eliminare un task.
// ○ Crea una funzione async handleToggleTask: deve fare una richiesta
// PATCH (/tasks/id) per aggiornare lo stato completed di un task.
// ○ Renderizza <TodoForm /> e <TodoList />, passando le funzioni e i dati
// necessari come props.


import React, { useState, useEffect } from 'react';
import TodoForm from './TodoForm';
import TodoList from './TodoList';

const API_URL = 'http://localhost:5340/tasks';

const TodoApp = () => {

    const [tasks, setTasks] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchTask = async () => {
        try {
            const response = await fetch(API_URL);
            if (!response.ok) throw new Error('Errore nella fetch')

            const data = await response.json();

            setTasks(data);

        } catch (err) {
            setError(err);

        } finally {
            setLoading(false);

        }
    };

    const deleteTask = async (id) => {
        await fetch(API_URL + '/' + id, { method: "DELETE" });
        fetchTask();
    };

    const toggleTask = async (id, completed) => {
        await fetch(API_URL + '/' + id, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ completed: !completed })
        });
        fetchTask();
    };

    useEffect(() => {
        fetchTask()
    }, [])

    return (
        <>
            <TodoForm />
            <TodoList tasks={tasks} onDeleteTask={deleteTask} onToggleTask={toggleTask} />
        </>
    )
}

export default TodoApp