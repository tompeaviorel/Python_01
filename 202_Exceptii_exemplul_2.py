def citeste_natural():
    try:
        n = int(input("Dati un numar natural in [1..100] n= "))
    except ValueError:
        raise ValueError("Acesta nu este un numar")
    if n < 0:
        raise ValueError("Numarul este negativ")
    if n > 100:
        raise ValueError("Numarul este prea mare")
    return n


def start():
    try:
        p = citeste_natural()
    except ValueError as mesaj_eroare:
        print(mesaj_eroare)
    else:
        print("am citit ", p)


start()
