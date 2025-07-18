from abc import ABC,abstractmethod
from my_tipes.my_general_tipes import *
from my_tipes.custom_types import *
from my_tipes.index import *
from tipi_di_dato_ebuy import *
from __future__ import annotations
from typing import Any
from datetime import datetime


class Utente(ABC):

    _username_usati = Index[str, Self]("username")

    def __init__(self,username:str):
        if self._username_usati.get(username) is not None:
            raise ValueError("username già usato") 
        self._username_usati.add(username, self)

        self._username = username #imm univoco
        self._registrazione = datetime.now() #imm
        

    def get_username(self) -> str:
        return self._username
    
    def _set_username(self, nuovo_username: str) -> None:
        if self._username_usati.get(nuovo_username) is not None:
            raise ValueError("username già usato")

        vecchio_username = self._username
        self._username = nuovo_username

        self._username_usati.remove(vecchio_username)
        self._username_usati.add(nuovo_username, self)


    def get_registrazione(self) -> datetime:
        return self._registrazione
    

    

class Privato(Utente):
    _tutti_link: set[_Bid_ut] = set()  

    def __init__(self, username):
        super().__init__(username)
        self._tutti_bid: set[_Bid_ut] = set()
        self._registrazione: datetime = datetime.now()

    def get_tutti_bid(self) -> frozenset[_Bid_ut]:
        return frozenset(self._tutti_bid)

    def _add_link_bid(self, l: _Bid_ut) -> None:
        self._tutti_bid.add(l)
        Privato._tutti_link.add(l)  

    def _remove_link_bid(self, l: _Bid_ut) -> None:
        self._tutti_bid.remove(l)
        Privato._tutti_link.remove(l)

    @classmethod
    def get_tutti_link(cls) -> frozenset[_Bid_ut]:
        return frozenset(cls._tutti_link)



class VenditoreProf(Utente):
    _tutti_link: set[_Pubblica] = set()

    def __init__(self, username,vetrina:URL):
        super().__init__(username)
        self._registrazione: datetime = datetime.now()
        self._vetrina = vetrina
        self._tutti_post: set[_Pubblica] = set()

    def get_vetrina(self) -> URL:
        return self._vetrina
    
    def set_vetrina(self,vetrina:URL) -> None:
        if isinstance(vetrina, URL):
            if vetrina != self.get_vetrina():
                self._vetrina = vetrina
            else:
                raise ValueError("quest'URL è già in uso")
        else:
            raise ValueError("la vetrina deve essere un URL")
        
    def get_tutti_post(self) -> FrozenSet[_Pubblica]:
        return frozenset(self._tutti_post)
    
    def _add_link_pubblica(self, l:_Pubblica) -> None:
        self._tutti_post.add(l)
        VenditoreProf._tutti_link.remove(l)

    def _remove_link_pubblica(self,l: _Pubblica) -> None:
        self._tutti_post.remove(l)
        VenditoreProf._tutti_link.remove(l)

    @classmethod
    def get_tutti_link(cls) -> frozenset[_Pubblica]:
        return frozenset(cls._tutti_link)
        

class PostOggetto(ABC):

    _tutti_venditori: set[_Pubblica] = set()

    def __init__(self, descrizione:str,prezzo:FloatGEZ,anni_garanzia:IntGEZ,venditoreProf:VenditoreProf,condizioni:Condizioni|None = None):
        self._descrizione = descrizione
        self._prezzo = prezzo
        self._condizioni = condizioni 
        self._is_nuovo: bool #imm
        if venditoreProf.get_registrazione() > datetime.now():
            raise ValueError("un post può essere pubblicato solo da un utente già registrato")
        self._venditoreProf = venditoreProf
        self._pubblicazione:datetime = datetime.now() #imm 

        self._set_is_nuovo()
        if self.get_is_nuovo() == True:
            if anni_garanzia < 2:
                raise ValueError("gli anni di garanzia devono essere >= 2")
                
        self._anni_garanzia = anni_garanzia
        self._feed: _Feed|None = None #non noto alla nascita

        self._link_venditoreProf: _Pubblica | None = None #imm
        Factory_pubblica.create_link(self, venditoreProf)
        

    def _set_is_nuovo(self) -> None:
        if self._condizioni is not None:
            self._is_nuovo = True
        else:
            self._is_nuovo = False


    def get_descrizione(self) -> str:
        return self._descrizione
    
    def get_prezzo(self) -> FloatGEZ:
        return self._prezzo
    
    def get_anni_garanzia(self) -> IntGEZ:
        return self._anni_garanzia
    
    def get_pubblicazione(self) -> datetime:
        return self._pubblicazione
    
    def get_condizioni(self) -> Condizioni:
        return self._condizioni
    
    def get_is_nuovo(self) -> bool:
        return self._is_nuovo
    
    def set_descrizione(self,descrizione:str) -> None:
        if isinstance(descrizione, str):
            if descrizione != self.get_descrizione():
                self._descrizione = descrizione
            else:
                raise ValueError("questa descrizione è già in uso")
        else:
            raise ValueError("la descrizione deve essere una stringa")

    def set_prezzo(self,prezzo:FloatGEZ) -> None:
        if isinstance(prezzo, FloatGEZ):
            if prezzo != self.get_prezzo():
                self._prezzo = prezzo
            else:
                raise ValueError("questo prezzo è già in uso")
        else:
            raise ValueError("il prezzo deve essere un FloatGEZ")
    
    def set_anni_garanzia(self,anni_garanzia:IntGEZ) -> None:
        if isinstance(anni_garanzia, IntGEZ):
            if anni_garanzia != self.get_anni_garanzia():
                self._anni_garanzia = anni_garanzia
            else:
                raise ValueError("questi anni di garanzia sono già in uso")
        else:
            raise ValueError("gli anni di garanzia devono essere un IntGEZ")
        
    def set_condizioni(self,condizioni:Condizioni) -> None:
        if isinstance(condizioni, Condizioni):
            if condizioni != self.get_condizioni():
                self._condizioni = condizioni
            else:
                raise ValueError("queste condizioni sono già in uso")
        else:
            raise ValueError("le condizioni devono essere un Condizioni")
        
    def get_feed(self) -> _Feed|None:
        return self._feed
    
    def get_feedback(self) -> Feedback|None:
        if self._feed is not None:
            return self.get_feed().get_feedback()

    def set_feedback(self,feedback:Feedback):
        if self.get_feed() is not None:
            if self.get_feedback() == feedback:
                raise ValueError("il feedback è già in uso")
        else:
            raise ValueError("il feedback è immutabile")
        
        self._feed = _Feed(self,feedback)
        feedback._set_feed(self._feed)

    def remove_feedback(self) -> None:
        if self._feed is not None:
            self._feed = None
        else:
            raise ValueError("il feed non è presente")
        
    def _add_link_pubblica(self, l: _Pubblica) -> None:
        self._link_venditoreProf = l
        PostOggetto._tutti_venditori.add(l)        

    def _remove_link_pubblica(self, l:_Pubblica) -> None:
        if self._link_venditoreProf == l:
            self._link_venditoreProf = None
            PostOggetto._tutti_venditori.remove(l)

    @classmethod
    def get_tutti_venditori(cls) -> frozenset[_Pubblica]:
        return frozenset(cls._tutti_venditori)

class Factory_pubblica:

    @classmethod
    def create_link(cls,postOggetto: PostOggetto, venditoreProf:VenditoreProf) -> None:
        l:_Pubblica = _Pubblica(postOggetto,venditoreProf)

    @classmethod
    def delete_link(cls,l:_Pubblica) -> None:
        if l is None: 
            raise ValueError("il link non può essere None")
        l.remove_pubblica()
        del l
        
class _Pubblica:

    def __init__(self, postOggetto: PostOggetto, venditoreProf:VenditoreProf):
        if postOggetto._link_venditoreProf is not None:
            raise ValueError("il postoggetto può essere pubblicato solo una volta")

        self._postOggetto = postOggetto
        self._venditoreProf = venditoreProf

        self.get_postOggetto()._add_link_pubblica(self)
        self.get_venditoreProf()._add_link_pubblica(self)

    def get_postOggetto(self) -> PostOggetto:
        return self._postOggetto
    
    def get_venditoreProf(self) -> VenditoreProf:
        return self._venditoreProf
    
    def remove_pubblica(self) -> None:
        if self in self.get_postOggetto().get_tutti_venditori() and self in self.get_venditoreProf().get_tutti_post():
            self.get_postOggetto()._remove_link_pubblica(self)
            self.get_venditoreProf()._remove_link_pubblica(self)


class Feedback:

    def __init__(self,voto:Voto,istante_voto:datetime,commento:str|None = None):
        self._voto = voto #imm
        self._commento = commento
        self._istante_voto = istante_voto #imm
        self._feed: _Feed|None = None #imm


    def get_voto(self) -> Voto:
        return self._voto
    
    def get_commento(self) -> str|None:
        return self._commento
    
    def get_istante_voto(self) -> datetime:
        return self._istante_voto
    
    def get_feed(self) -> None|PostOggetto:
        return self._feed
    
    
    def set_commento(self,commento:str) -> None:
        if isinstance(commento, str):
            if commento != self.get_commento():
                self._commento = commento
            else:
                raise ValueError("questo commento è già in uso")
        else:
            raise ValueError("il commento deve essere una stringa")
    
    def _set_feed(self,feed:_Feed):
        if self._feed is None:
            self._feed = feed
        else:
            raise ValueError("il Feedback appartiene ad una altro PostOggetto")

class _Feed:

    def __init__(self,postOggetto:PostOggetto,feedback:Feedback):
        self._postOggetto = postOggetto
        self._feedback = feedback


    def get_postOgetto(self) -> PostOggetto:
        return self._postOggetto
    
    def get_feedback(self) -> Feedback:
        return self._feedback
    

class Asta(PostOggetto):
    _tutti_link: set[_Asta_bid] = set()

    def __init__(self, descrizione, prezzo, anni_garanzia,prezzo_bid:FloatGEZ,scadenza:datetime,venditoreProf:VenditoreProf, condizioni = None):
        super().__init__(descrizione, prezzo, anni_garanzia, condizioni, venditoreProf)
        if scadenza < datetime.now():
            raise ValueError("la scadenza non può precedere la pubblicazione")

        self._pubblicazione = datetime.now()
        self._prezzo_bid = prezzo_bid
        self._scadenza = scadenza
        self._tutte_aste: set[_Asta_bid] = set()

    def get_tutte_aste(self) -> frozenset[_Asta_bid]:
        return frozenset(self._tutte_aste)

    def get_scadenza(self) -> datetime:
        return self._scadenza

    def get_prezzo_bid(self) -> FloatGEZ:
        return self._prezzo_bid

    def set_prezzo_bid(self,prezzo_bid:FloatGEZ) -> None:
        if isinstance(prezzo_bid, FloatGEZ):
            if prezzo_bid != self.get_prezzo_bid():
                self._prezzo_bid = prezzo_bid
            else:
                raise ValueError("questo prezzo_bid è già in uso")
        else:
            raise ValueError("il prezzo_bid deve essere un FloatGEZ")
    
    def set_scadenza(self,scadenza: datetime) -> None:
        if isinstance(scadenza, datetime):
            if scadenza != self.get_scadenza():
                self._scadenza = scadenza
            else:
                raise ValueError("questa scadenza è già in uso")
        else:
            raise ValueError("la scadenza deve essere un datetime")
        
    def _add_link_asta(self, l:_Asta_bid) -> None:
        self._tutte_aste.add(l)
        Asta._tutti_link.add(l)

    def _remove_link_asta(self, l:_Asta_bid) -> None:
        self._tutte_aste.remove(l)
        Asta._tutti_link.remove(l)
        
    @classmethod
    def get_tutti_link(cls) -> frozenset[_Asta_bid]:
        return frozenset(cls._tutti_link)

class Bid:
    _tutti_privati: set[_Bid_ut] = set()  
    _tutte_aste: set[_Asta_bid] = set()

    def __init__(self, privato: Privato, asta:Asta):
        if privato.get_registrazione() > datetime.now():
            raise ValueError("il bid va creato dopo la nascita del privato")
        if asta.get_scadenza() < datetime.now():
            raise ValueError("il bid va creato prima della scadenza dell'asta")
        
        self._istante:datetime = datetime.now()  # imm
        self._link_privato: _Bid_ut | None = None  
        Factory_bid_ut.create_link(self, privato)

        self._link_asta: _Asta_bid | None = None
        Factory_asta_bid.create_link(self, asta)



    def get_istante(self) -> datetime:
        return self._istante
    
    def get_tutti_privati(self) -> frozenset[_Bid_ut]:
        return frozenset(self._tutti_privati)

    def get_tutte_aste(self) -> frozenset[_Asta_bid]:
        return frozenset(self._tutte_aste)
    
    def _add_link_bid(self, l: _Bid_ut) -> None:
        self._link_privato = l
        Bid._tutti_privati.add(l)

    def _remove_link_bid(self, l: _Bid_ut) -> None:
        if self._link_privato == l:
            self._link_privato = None
            Bid._tutti_privati.remove(l)
            
    def appartiene(self, privato: Privato) -> bool:
        return any(link.get_privato() == privato for link in Bid._tutti_privati if link.get_bid() == self)

    
    def _add_link_asta(self, l: _Asta_bid) -> None:
        self._link_asta = l
        Bid._tutte_aste.add(l)

    def _remove_link_asta(self,l: _Asta_bid) -> None:
        if self._link_asta == l:
            self._link_asta = None
            Bid._tutte_aste.remove(l)
    
class Factory_bid_ut:

    @classmethod
    def create_link(cls,bid:Bid, privato:Privato) -> None:
        l:_Bid_ut = _Bid_ut(bid,privato)

    @classmethod
    def delete_link(cls,l:_Bid_ut) -> None:
        if l is None: 
            raise ValueError("il link non può essere None")
        l.remove_bid_ut()
        del l
    

class _Bid_ut:

    def __init__(self, bid:Bid, privato:Privato):
        if bid._link_privato is not None:
            raise ValueError("il bid può appartenere ad un solo privato")

        self._bid = bid
        self._privato = privato

        self.get_privato()._add_link_bid(self)
        self.get_bid()._add_link_bid(self)


    def get_privato(self) -> Privato:
        return self._privato

    def get_bid(self) -> Bid:
        return self._bid     
    
    def remove_bid_ut(self) -> None:
        if self in self.get_bid().get_tutti_privati() and self in self.get_privato().get_tutti_bid():
            self.get_bid()._remove_link_bid(self)
            self.get_privato()._remove_link_bid(self)

class Factory_asta_bid:

    @classmethod
    def create_link(cls,bid:Bid, asta:Asta) -> None:
        l:_Asta_bid = _Asta_bid(bid,asta)

    @classmethod
    def delete_link(cls,l:_Asta_bid) -> None:
        if l is None: 
            raise ValueError("il link non può essere None")
        l.remove_asta_bid()
        del l
    
class _Asta_bid:

    _link_asta_usati: set[tuple[Bid, Asta]] = set()

    def __init__(self, bid: Bid, asta: Asta):
        coppia = (bid, asta)

        if coppia in self._link_asta_usati:
            raise ValueError("il link tra questo Bid e questa Asta esiste già")

        if bid._link_asta is not None:
            raise ValueError("il bid può appartenere ad una sola asta")

        self._bid = bid
        self._asta = asta

        self.get_bid()._add_link_asta(self)
        self.get_asta()._add_link_asta(self)

        self.__class__._link_asta_usati.add(coppia)

    def get_bid(self) -> Bid:
        return self._bid 
    
    def get_asta(self) -> Asta:
        return self._asta
    
    def remove_asta_bid(self) -> None:
        coppia = (self._bid, self._asta)

        if self in self.get_bid().get_tutte_aste() and self in self.get_asta().get_tutte_aste():
            self.get_bid()._remove_link_asta(self)
            self.get_asta()._remove_link_asta(self)
            self.__class__._link_asta_usati.discard(coppia)


# ricorda l'assimetria verso bid sia in bid_ut che asta_bid (ciò non compromette la responsabilità doppia in entrambi i casi)
# per implementarla bisogna incorporare l class_factory all'interno di bid stesso, mettendo il create_link come privato e richiamandolo nell'init        
    
    
    
