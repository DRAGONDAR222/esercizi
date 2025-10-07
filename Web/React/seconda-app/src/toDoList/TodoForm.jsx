// 2. TodoForm.js (Figlio):
// ○ Riceve la funzione handleAddTask come prop.
// ○ Contiene un form con un input di testo controllato per il nuovo task.
// ○ Alla sottomissione del form, chiama handleAddTask con il testo dell'input.


import { useRef } from "react";
import { useTodos } from "./useTodos";


const TodoForm = () => {
  const {addTask:onAddTask}=useTodos()
  const textRef=useRef(null);
  const handleSubmit= (e)=>{
      e.preventDefault()
      if(textRef.current.value.trim()){
        onAddTask(textRef.current.value);
        textRef.current.value="";
      }else{
        alert("Inserisci un task")
      }
  }
  return (
    <form className='d-flex mb-3' onSubmit={handleSubmit}>
      <input type="text" className='form-control me-3' ref={textRef}>
      </input>
      <button className="btn btn-primary">Salva task</button>
    </form>
  )
}

export default TodoForm