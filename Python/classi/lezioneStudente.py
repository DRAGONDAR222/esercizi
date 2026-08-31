from lezioneP import Persona

class Studente(Persona):

  ''' def inheritanceTest(self):
        # verifichiamo l'ereditarit├á
        self.nome
        self.cognome
        self.et├á

        # anche dei metodi
        self.getNomePersona()
        self.getCognomePersona()
        self.getEt├áPersona() '''
   


   
  #inizializzare un oggetto classe studente
  def __init__(self, nome:str, cognome:str, et├á:int, matricola:str):
          # inizializza la superclasse
    super().__init__(nome, cognome, et├á)

      # inizializzare la classe studente
      # istruzioni che inizializzano uno studente
    self.setMatricola(matricola)

      # metodi setter

      # metodo che ci consente di impostare il valore dell'attributo self.matricola
  def setMatricola(self,matricola:str) -> None:
          
          # se la stringa non ├¿ vuota
          if matricola:
              self.matricola = matricola
          else:
            print("errore la matricola non pu├▓ essere una stringa vuota")

  def getMatricola(self) -> str:
      return self.matricola


  # metodo che consente di visualizzare le informazioni relative ad un oggetto della classe Studente
  def __str__(self) ->str:
      return f"\nNome: {self.getNomePersona()}\nCognome: {self.cognome}\nMatricola: {self.getMatricola()}"

  # metodo che mi consente di calcolare la media degli esami sostenuti de uno studente:
  def getMediaEsami(self,voti_esami:list[int]) -> float:
      
      # se la lista non ├¿ vuota 
      if voti_esami:
        # calcolare la somma dei voti
        somma:int = 0
        for voto in voti_esami:
            somma += voto
        
        # ritornare la media 
        return round(somma/len(voti_esami), 2)
      # se la lista ├¿ vuota
      else:
            return 0.00
      
  # metodo che consente di confrontare 2 oggetti della classe Studente e stabilire se questi due oggetti suano uguali o meno
  # due studenti 
  def __eq__(self,other) -> bool:
      #se other ├¿ None, oppure se oother ├¿ un'istanza della classe Studente ritorno False
      if other is None or not isinstance(other, type(self)):
          return False
      # altrimenti valuta la seguentwe ugualianza
      else:
          return self.getMatricola() == other.getMatricola()
      

