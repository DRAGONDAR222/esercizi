from abc import ABC,abstractmethod


class Volo(ABC):
    _codice: str
    _capacità_massima:int
    _prenotazioni: int

    @abstractmethod
    def __init__(self,codice:str,capacità_massima:int):
        self._codice = self.set_codice(codice)
        self._capacità_massima = self.set_capacità_massima(capacità_massima)
        self._prenotazioni = 0

    @abstractmethod
    def prenota_posto(self):
        pass

    @abstractmethod
    def posti_disponibili(self) -> int:
        pass

    
    def get_codice(self) -> str:
        return self._codice
    
    
    def get_capacità_massima(self) -> int:
        return self._capacità_massima
    
    
    def get_prenotazioni(self) -> int:
        return self._prenotazioni
    
    
    def set_codice(self,codice:str) -> None:
        self.get_codice = codice

    
    def set_capacità_massima(self,capacità_massima:int) -> None:
        self._capacità_massima = capacità_massima

    
    def set_prenotazioni(self,prenotazioni:int) -> None:
        self._prenotazioni = prenotazioni

class VoloCommerciale(Volo):
    _posti_economica:int
    _posti_buisiness:int
    _posti_prima:int

    def __init__(self, codice, capacità_massima):
        super().__init__(codice, capacità_massima)

        self._posti_economica = self._capacità_massima // 0.7
        self._posti_buisiness = self._capacità_massima // 0.2
        self._posti_prima = self._capacità_massima // (1.0 -0.2 - 0.7)

    def get_posti_economica(self) -> int:
        return self._posti_economica
    
    def get_posti_business(self) -> int:
        return self._posti_buisiness
    
    def get_posti_prima(self) -> int:
        return self._posti_prima

    def posti_disponibili(self) -> dict[str,int]:
        dict_posti:dict[str,int] = {"posti disponibili": 0,"classe economica": 0,"classe business": 0,"prima classe": 0}
        
        dict_posti["posti disponibili"] = self.get_capacità_massima()
        dict_posti["classe economica"] = self.get_posti_economica()
        dict_posti["classe business"] = self.get_posti_business()
        dict_posti["prima classe"] = self.get_posti_prima()

        return dict_posti
    
    def prenota_posto(self,posti:int,classe_servizio:str) -> None:

        if self.posti_disponibili()["posti disponibili"] > 0:
            if self.posti_disponibili()[f"{classe_servizio}"]:
                if posti <= self.posti_disponibili()[f"{classe_servizio}"]:
                    self.posti_disponibili()[f"{classe_servizio}"] -= posti
                    self.posti_disponibili()["posti disponibili"] -= posti
                    if self.posti_disponibili()[f"{classe_servizio}"] < 0:
                        self.posti_disponibili()[f"{classe_servizio}"] = 0
                    elif self.posti_disponibili()["posti disponibili"] < 0:
                        self.posti_disponibili()["posti disponibili"] = 0
                    print(f"ho riservato {posti} nella classe {classe_servizio} codice volo:{self.get_codice()}")
                else: print("non ci sono più posti disponibili nella classe scelta")
            else: print("la chiave richiesta non è valida")
        else:
            print("il volo è al completo")

class VoloCharter(Volo):
    _costo_volo:float
    
    def __init__(self, codice, capacità_massima, costo_volo:float):
        super().__init__(codice, capacità_massima)
        self._costo_volo = costo_volo
    
    def get_costo_volo(self) -> float:
        return self._costo_volo
    
    def set_costo_volo(self,costo_volo:float) -> None:
        self._costo_volo = costo_volo

    def prenota_posto(self):
        if self.get_prenotazioni() == self.get_capacità_massima():
            self._prenotazioni = self._capacità_massima
            print(f"il volo {self.get_codice()} è stato prenotato a buon fine, hai pagato: {self.get_costo_volo()}")
        else:
            print("il volo charter è già stato prenotato")
    
    def posti_disponibili(self):
        return super().posti_disponibili()
    

class CompagniaAerea:
    _nome_compagnia:str
    _prezzo_standard:float
    _flotta:list[VoloCommerciale] = []

    def __init__(self,nome:str,prezzo:float):
        self._nome_compagnia = nome
        self._prezzo_standard = prezzo

    def aggiungi_volo(self, volo:VoloCommerciale) -> None:
        self._flotta

        


       
    