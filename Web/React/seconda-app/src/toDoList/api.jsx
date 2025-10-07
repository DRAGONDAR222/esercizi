const API_URL = 'http://localhost:5340/tasks';
// comando di avvio server
// json-server db.json --watch --port 5340


export const fetchTasksService = async () => {
  const response = await fetch(API_URL);
  if (!response.ok) throw new Error("Errore nella fetch");
  const data = await response.json();
  return data;
};

export const deleteTaskService = async (id) => {
  await fetch(API_URL + "/" + id, { method: "DELETE" });
};

export   const toggleTaskService = async (id, completed) => {
    await fetch(API_URL + "/" + id, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ completed: !completed }),
    });

  };

export  const addTaskService = async (text) => {
    await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, completed: false }),
    });
  
  };

export  const updateTaskService = async (id, text) => {
    await fetch(API_URL + "/" + id, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
  
  };