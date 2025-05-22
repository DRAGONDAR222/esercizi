from formagenerica import FormaGenerica

class Rettangolo(FormaGenerica):

    # inizializzare un oggetto della classe Rettangolo
    def __init__(self):
        super().__init__()

        self.setShape('rettangolo')

    def draw(self) -> None:

        print(f"\n{self.getShape()}\n")


        # outer for
        for i in range(5):
            # inner for
            for j in range(5*2):

                # il lato a e il lato d del rettangolo
                if i == 0 or i == 5-1:
                    print("*",end=" ")
                # il lato b e il lato c del rettangolo
                elif j == 0 or j == 5*2 -1:
                    print("*", end =" ")
                # spazi bianchi
                else:
                    print(" ", end = " ")
            print("\n", end= "")