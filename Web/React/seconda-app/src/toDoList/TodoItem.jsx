// 4. TodoItem.js (Nipote):
// ○ Riceve il singolo oggetto task e le funzioni handleDeleteTask e
// handleToggleTask come props.
// ○ Visualizza il testo del task. Applica uno stile per sbarrare il testo se
// task.completed è true.
// ○ Aggiungi un checkbox che, al onChange, chiami handleToggleTask con
// l'id e lo stato completed invertito.
// ○ Aggiungi un bottone "Elimina" che, al onClick, chiami handleDeleteTask
// con l'id del task.

import React, { useState } from "react";
import { useTodos } from "./useTodos";

const TodoItem = ({ task}) => {
  const {deleteTask,toggleTask,updateTask}=useTodos();
  const [isEditing, setIsEditing] = useState(false);
  const [editText, setEditText] = useState(task.text);
  const handleSave = () => {
    console.log(editText);
    if (editText.trim()) {
      updateTask(task.id, editText);
      setIsEditing(false);
    } else {
      setIsEditing(false);
    }
  };
  return (
    <li className="list-group-item d-flex justify-content-between">
      {isEditing ? (
        <div>
          <input
            type="text"
            className="form-control d-inline-block"
            value={editText}
            onChange={(e) => setEditText(e.target.value)}
            onBlur={handleSave}
            style={{ width: "300px", marginRight: "3px" }}
            addTaskServiceaddTaskService
          ></input>
          <button
            onClick={() => setIsEditing(false)}
            className="btn btn-danger"
            style={{ marginTop: "-6px" }}
          >
            X
          </button>
        </div>
      ) : (
        <div>
          <input
            type="checkbox"
            className="form-check-input me-2"
            checked={task.completed}
            onChange={() => {
              toggleTask(task.id, task.completed);
            }}
          ></input>
          <span
            onDoubleClick={() => setIsEditing(true)}
            style={{ textDecoration: task.completed ? "line-through" : "none" }}
          >
            {task.text}
          </span>
        </div>
      )}

      <button className="btn btn-danger" onClick={() => deleteTask(task.id)}>
        Delete
      </button>
    </li>
  );
};

export default TodoItem;