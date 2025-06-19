from typing import Self

class Frazione:
    __numeratore:int
    __denominatore:int

    def __init__(self,numeratore:float,denominatore:float) -> Self:
        self.__numeratore = self.set_numeratore(numeratore)
        self.__denominatore = self.set_denominatore(denominatore)

    
    def str(self) -> str:
        return f"{self.__numeratore}/{self.__denominatore}"
    
    def repr(self) -> str:
        return f"{self.__numeratore}/{self.__denominatore}"

    def value(self) -> float:
        return round(self.__numeratore/self.__denominatore, 3)
    
    def set_numeratore(self,numeratore:float = 13) -> None:
        if isinstance(numeratore, int):
            self.__numeratore = numeratore

    def set_denominatore(self,denominatore:float = 5) -> None:
        if isinstance(denominatore, int) and denominatore != 0:
            self.__denominatore = denominatore
        elif denominatore == 0:
            self.__denominatore = 5

    def get_numeratore(self) -> int:
        return self.__numeratore

    def get_denominatore(self) -> int:
        return self.__denominatore
    
    def mcd(self,x:int,y:int) -> int:
        mcd:int = 1

        if x > y:
            minimo = y
        else:
            minimo = x

        for i in range(2,minimo + 1):
            if x % i == 0 and y % i == 0:
                mcd = i
                return mcd

        return mcd
    
    def semplifica(self,lista_frazioni:list[Self]) -> list[Self]:
        l:list[Self] = []
        for frazione in lista_frazioni:
            if self.mcd(frazione.get_numeratore(), frazione.get_denominatore()) == 1:
                l.append(frazione)

            else:
                m_divisore:int = self.mcd(frazione.get_numeratore(), frazione.get_denominatore())
                num = frazione.get_numeratore() / m_divisore
                den = frazione.get_denominatore() / m_divisore
                l.append(Frazione(num,den))     

        return l
if __name__ == '__main__':
    f1 = Frazione(10,2)
    print(f1)
    print(f1.value())

    f2 = Frazione(0,0)
    print(f2)
    print(f2.value())

    f3 = Frazione(4.5,2)
    print(f3)
    print(f3.value())

    print(f1.mcd(12,18))

    print(f1.semplifica([Frazione(1,1), Frazione(12,18),Frazione(5,7), Frazione(2,8)]))    


        


