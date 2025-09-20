from __future__ import annotations

class Film:
    __id:int
    __title:str


    def __init__(self, id:int, title:str) -> None:
        self.setID(id)
        self.setTitle(title)


    def setID(self,id:int) -> None:
        self.__id = id

    def setTitle(self,title:str) -> None:
        self.__title = title

    
    def getID(self) -> int:
        return self.__id
    
    def getTitle(self) -> str:
        return self.__title
    

    def isEqual(self,otherFilm:Film) -> bool:
        return True if self.getID() == otherFilm.getID() else False
    
