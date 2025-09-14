import re

class ProjectManager:

    def __init__(self):
        self.projects: dict[str,list[dict[str,str|bool]]] = {}

    def create_projects(self, project_name:str) -> dict|str:

        if project_name in self.projects:
            return f'Errore, il progetto esiste già'
        
        self.projects[project_name] = []

        return {project_name: self.projects[project_name]}
    
    
    def add_task(self, project_name:str, task_name:str, description:str) -> dict|str:

        if project_name not in self.projects:
            return f'Errore, il progetto non esiste'
        
        # per ogni dizionario nella lista
        for task in self.projects[project_name]:
            if task_name == task['name']:
                return f'Errore, il task è già presente'
            
        self.projects[project_name].append({'name':task_name, 'description':description, 'done':False})

        return {project_name: self.projects[project_name]}
    

    def complete_task(self, project_name:str, task_name:str) -> dict|str:

        if project_name not in self.projects:
            return f'Errore, il progetto non esiste'
        
        for task in self.projects[project_name]:
            if task_name == task['name']:
                task['done'] = True
                return {project_name: self.projects[project_name]}
        
        return f'Errore, il task non esiste'
    

    def remove_task(self, project_name: str, task_name: str) -> dict | str:
        if project_name not in self.projects:
            return 'Errore, il progetto non esiste'
        
        for task in self.projects[project_name]:
            if task['name'] == task_name:
                self.projects[project_name].remove(task)
                return {project_name: self.projects[project_name]}
            
        return 'Errore, il task non è presente'

    
    def list_projects(self) -> list[str]:

        return self.projects.keys()
    

    def list_task(self, project_name:str) -> list[str]|str:
        
        if project_name not in self.projects:
            return f'Errore, il progetto non esiste'

        my_list:list[str] = [task['name'] for task in self.projects[project_name]]
         
        if not my_list:
            return 'Errore, la lista è vuota'
        
        return my_list
    

    def get_task_info(self, project_name:str, task_name:str) -> dict|str:

        if project_name not in self.projects:
            return f'Errore, il progetto non esiste'
        
        for task in self.projects[project_name]:
            if task_name == task['name']:
                return task
            
        return f'Errore, il task non è presente'
            

    def search_task_by_description(self, keyword:str) -> list[tuple[str,dict[str,str|bool]]]|str:

        my_list:list[tuple] = []

        for project in self.projects:
            for task in self.projects[project]:
                if re.search(fr'{keyword}', task['description']):
                    my_list.append((project,task))

        if not my_list:
            return f'Errore, non è stato trovato nulla'
        
        return my_list
                    
            