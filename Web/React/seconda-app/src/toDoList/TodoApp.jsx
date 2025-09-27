import React, { useEffect, useState } from 'react'
import TodoForm from './TodoForm'
import TodoList from './TodoList'

const API_URL = 'http://localhost:5340';

const TodoApp = () => {
    const [tasks, setTasks] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchTasks = async () => {
        try {
            const response = await fetch(API_URL);
            if (!response.ok) throw new Error('Errore nella fetch')

            const data =  await response.json();
            setTasks(data);
            

        } catch (err) {
            setError(err)
        } finally {
            setLoading(false)
        }
    };

    const deleteTask=async (id)=>{
        await fetch(API_URL+'/'+id,{method:'DELETE'});
        fetchTasks();
    }

    useEffect(() => { fetchTasks() }, []);

    const toggleTask=async(id,completed)=>{
        await fetch(API_URL+'/'+id),{
            method:'PATCH',
            headers:{'Content-Type':'application/json'},
            body:JSON.stringify({completed:!completed})
        } 
        fetchTasks();
    };

    return (
        <div>
            <TodoForm></TodoForm>
            <TodoList tasks={tasks} onDeleteTask={deleteTask} onToggleTask={toggleTask}></TodoList>
        </div>
    )
}

export default TodoApp