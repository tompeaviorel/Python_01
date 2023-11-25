"""
    Definirea de exceptii utilizator
    preluat de pe :
    https://uncoded.ro/erori-si-exceptii-in-limbajul-python/
"""


class Eroare(Exception):
    # Clasa de baza pentru exceptii de utilizator
    pass


class FonduriInsuficiente(Eroare):
    # Exceptie generata cand soldul unui cont este mai mic decat suma solicitata"
    pass


class Cont:
    def __init__(self, numar, sold):
        self.numar = numar
        self.sold = sold

    def __str__(self):
        return "Contul {} are un  sold de {} RON.".format(self.numar, round(self.sold, 2))

    def depune(self, suma):
        self.sold += suma

    def retrage(self, suma):
        try:
            if self.sold >= suma:
                self.sold -= suma
            else:
                necesar = suma - self.sold
                raise FonduriInsuficiente("Fonduri insuficiente! Necesar {} RON.".format(round(necesar, 2)))
        except FonduriInsuficiente as e:
            print(e)


if __name__ == "__main__":
    c = Cont("SV523BTV74635643", 500.34)
    # Contul SV523BTV74635643 are un sold de 500.34 RON.
    print(c)
    c.depune(20.12)
    # Fonduri insuficiente! Necesar 502.63 RON.
    c.retrage(1023.09)
