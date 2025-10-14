import { createContext,useState,useEffect } from "react";
import { fetchTasksService,deleteTaskService,toggleTaskService,addTaskService,updateTaskService } from "./api";



const TodoContext=createContext();


export function TodoProvider({children}){
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const fetchTasks = async () => {
      try {
        const data = await fetchTasksService();
        setTasks(data);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };
  
    const deleteTask = async  (id) => {
      await deleteTaskService(id);
      fetchTasks();
    };
  
    const toggleTask = async (id, completed) => {
      await toggleTaskService(id, completed);
      fetchTasks();
    };
    
    const addTask = async (text) => {
      await addTaskService(text)
      fetchTasks();
    };
  const updateTask = async (id, text) => {
      await updateTaskService (id, text)
      fetchTasks();
    };
    useEffect(() => {
      fetchTasks();
    }, []);

    return(
        <TodoContext.Provider
            value={
                {tasks,loading,error,deleteTask,toggleTask,addTask,updateTask}
            }
        >
            {children}
        </TodoContext.Provider>
    )
}

export default TodoContext;