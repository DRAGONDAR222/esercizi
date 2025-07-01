from abc import ABC, abstractmethod

class Volo(ABC):
    _codice: str
    _capacità_massima: int
    _prenotazioni: int

    @abstractmethod
    def __init__(self, codice: str, capacità_massima: int):
        self._codice = codice
        self._capacità_massima = capacità_massima
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

    def set_capacità_massima(self, capacità_massima: int) -> None:
        self._capacità_massima = capacità_massima

    def set_prenotazioni(self, prenotazioni: int) -> None:
        self._prenotazioni = prenotazioni


class VoloCommerciale(Volo):
    _posti_economica: int
    _posti_buisiness: int
    _posti_prima: int

    def __init__(self, codice, capacità_massima):
        super().__init__(codice, capacità_massima)
        self._posti_economica = int(self._capacità_massima * 0.7)
        self._posti_buisiness = int(self._capacità_massima * 0.2)
        self._posti_prima = self._capacità_massima - self._posti_economica - self._posti_buisiness

        self._prenotati_economica = 0
        self._prenotati_buisiness = 0
        self._prenotati_prima = 0

    def get_posti_economica(self) -> int:
        return self._posti_economica

    def get_posti_business(self) -> int:
        return self._posti_buisiness

    def get_posti_prima(self) -> int:
        return self._posti_prima

    def posti_disponibili(self) -> dict[str, int]:
        dict_posti: dict[str, int] = {"posti disponibili": 0,"classe economica": 0,"classe business": 0,"prima classe": 0}

        dict_posti["classe economica"] = self._posti_economica - self._prenotati_economica
        dict_posti["classe business"] = self._posti_buisiness - self._prenotati_buisiness
        dict_posti["prima classe"] = self._posti_prima - self._prenotati_prima
        dict_posti["posti disponibili"] = (dict_posti["classe economica"] + dict_posti["classe business"] + dict_posti["prima classe"])

        return dict_posti

    def prenota_posto(self, posti: int, classe_servizio: str) -> None:
        disponibili = self.posti_disponibili()
        if disponibili["posti disponibili"] > 0:
            if classe_servizio in disponibili:
                if posti <= disponibili[classe_servizio]:
                    if classe_servizio == "classe economica":
                        self._prenotati_economica += posti
                    elif classe_servizio == "classe business":
                        self._prenotati_buisiness += posti
                    elif classe_servizio == "prima classe":
                        self._prenotati_prima += posti
                    print(f"ho riservato {posti} nella classe {classe_servizio} codice volo:{self.get_codice()}")
                else:
                    print("non ci sono più posti disponibili nella classe scelta")
            else:
                print("la chiave richiesta non è valida")
        else:
            print("il volo è al completo")


class VoloCharter(Volo):
    _costo_volo: float

    def __init__(self, codice, capacità_massima, costo_volo: float):
        super().__init__(codice, capacità_massima)
        self._costo_volo = costo_volo
        self._prenotato = False

    def get_costo_volo(self) -> float:
        return self._costo_volo

    def set_costo_volo(self, costo_volo: float) -> None:
        self._costo_volo = costo_volo

    def prenota_posto(self):
        if not self._prenotato:
            self._prenotazioni = self._capacità_massima
            self._prenotato = True
            print(f"il volo {self.get_codice()} è stato prenotato a buon fine, hai pagato: {self.get_costo_volo()}")
        else:
            print("il volo charter è già stato prenotato")

    def posti_disponibili(self):
        return self.get_capacità_massima() - self.get_prenotazioni()


class CompagniaAerea:
    _nome_compagnia: str
    _prezzo_standard: float
    _flotta: list[VoloCommerciale]

    def __init__(self, nome: str, prezzo: float):
        self._nome_compagnia = nome
        self._prezzo_standard = prezzo
        self._flotta = []

    def get_prezzo_standard(self) -> float:
        return self._prezzo_standard

    def get_flotta(self) -> list[VoloCommerciale]:
        return self._flotta

    def aggiungi_volo(self, volo: VoloCommerciale) -> None:
        self._flotta.append(volo)

    def rimuovi_volo(self, volo: VoloCommerciale) -> None:
        if volo in self.get_flotta():
            self._flotta.remove(volo)

    def mostra_flotta(self) -> str:
        for i in self.get_flotta():
            print(f"codice volo: {i.get_codice()}")

    def guadagno(self) -> float:
        guadagno_totale: float = 0.00
        for aereo in self.get_flotta():
            for economica in range(aereo.get_posti_economica() - aereo.posti_disponibili()["classe economica"]):
                guadagno_totale += self.get_prezzo_standard()
            for business in range(aereo.get_posti_business() - aereo.posti_disponibili()["classe business"]):
                guadagno_totale += (self.get_prezzo_standard() * 2)
            for prima in range(aereo.get_posti_prima() - aereo.posti_disponibili()["prima classe"]):
                guadagno_totale += (self.get_prezzo_standard() * 3)
        return round(guadagno_totale, 2)


        


       
    