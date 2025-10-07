// 3. TodoList.js (Figlio):
// ○ Riceve tasks, handleDeleteTask e handleToggleTask come props.
// ○ Mappa l'array tasks e, per ogni task, renderizza un componente <TodoItem
// /> passandogli i dati e le funzioni necessarie.


import React from "react";
import TodoItem from "./TodoItem";
import { useTodos } from "./useTodos";

const TodoList = () => {

  const {tasks}=useTodos()
  return (
    <ul className="list-group">
      {tasks.map((t) => {
        return (
          <TodoItem
            key={t.id}
            task={t}
           
          ></TodoItem>
        );
      })}
    </ul>
  );
};

export default TodoList;