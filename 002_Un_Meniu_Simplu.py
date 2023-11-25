"""
    Citeste o lista de numere si afiseaza numerele prime.
    Creati un meniu:
    1. Citeste lista de numere
    2. Iesire
"""


def este_prim(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def afisare_prime(v):
    print("PRIME : ", end=" ")
    for e in v:
        if este_prim(e):
            print(e, end=" ")
    print()


def meniu():
    while True:
        print("1. Citeste lista de numere: ")
        print("2. Iesire")
        optiune = input(">")
        if optiune == "1":
            sir_de_numere = input("Introduceti o lista de numere separate prin spatiu")
            lista_numere = sir_de_numere.split()
            lista_intregi = []  #
            # transforma lista de numere (memorata ca lista de siruri de caractere, in lista de intregi)
            for e in lista_numere:
                lista_intregi.append(int(e))

            print(sir_de_numere)
            print(lista_numere)
            print(lista_intregi)
            afisare_prime(lista_intregi)
        elif optiune == "2":
            print("bye")
            break
        else:
            print("Optiune gresita. Alege 1 sau 2 !")


if __name__ == '__main__':
    meniu()
