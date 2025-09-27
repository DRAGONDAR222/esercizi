import React from 'react'

const TodoItem = ({ task, onDeleteTask, onToggleTask }) => {
    return (
        <li className='list-group-item d-flex justify-content-between'>
            <div>
                <input type='checkbox'
                    className='form-check-input me-2'
                    checked={task.completed}
                    onChange={() => {
                        onToggleTask(task.id, task.completed);
                    }}>
                </input>

                <span style={{ textDecoration: task.copleted ? 'line-throught' : 'none' }}>
                    {task.text}</span>
            </div>
            <button className='btn btn-danger'
                onClick={() => onDeleteTask(task.id)}>
                Delete
            </button>
        </li>
    )
}

export default TodoItem