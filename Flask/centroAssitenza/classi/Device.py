from abc import ABC, abstractmethod
import StatusEnum

class Device(ABC):

    id: str
    model: str
    customer_name: str
    purchase_year: int
    status: StatusEnum

    def __init__(self, id, model, customer_name, purchase_year, status: StatusEnum):
        self.id = id
        self.model = model
        self.customer_name = customer_name
        self.purchase_year = purchase_year
        
        if not isinstance(status, StatusEnum):
            raise ValueError(f"Status '{status}' non valido. Deve essere un StatusEnum.")
        self.status = status

    @abstractmethod
    def device_type(self):
        pass
    
    @abstractmethod
    def base_diagnosis_time(self):
        pass
    
    @abstractmethod
    def repair_complexity(self):
        pass
    
    def info(self):
        return {
            "id": self.id,
            "device_type": self.device_type(),
            "model": self.model,
            "customer_name": self.customer_name,
            "purchase_year": self.purchase_year,
            "status": self.status.value,       # il valore dell'enum, es: "received"
            "status_name": self.status.name   # il nome dell'enum, es: "RICEVUTO"
        }
    
    def estimated_total_time(self, factor: float = 1.0):
        return self.base_diagnosis_time() * factor + self.repair_complexity() * 30
