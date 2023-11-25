import copy


def copiere(la):
    lb = []
    for d in la:
        x = {"unu": d['unu'], "doi": d['doi'], "trei": d['trei']}

        lb.append(x)
    return lb


def afisare(ld):
    for linie in ld:
        print(linie['unu'], linie['doi'], linie['trei'])


def test1():
    print("test 1 : FUNCTIA DE COPIERE PROPRIE lista_2 = copiere(lista_1)")
    lista_1 = [{"unu": 10, "doi": 20, "trei": 30}, {"unu": 40, "doi": 50, "trei": 60}]
    print(lista_1)
    afisare(lista_1)

    lista_2 = copiere(lista_1)
    afisare(lista_2)

    print("lista 1", lista_1)
    print("lista 2", lista_2)
    print("adresa lista 1", id(lista_1))
    print("adresa lista 2", id(lista_2))
    print("adresa lista1[0]", id(lista_1[0]))
    print("adresa lista2[0]", id(lista_2[0]))

    lista_1[0]['unu'] = -4
    print("lista 1", lista_1)
    print("lista 2", lista_2)
    print("ADRESA DE START A LISTEI ESTE DIFERITA. ...OK")
    print("ADRESA DE START A SUBLISTELOR ESTE DIFERITA. ...OK")


def test2():
    print("test 2 : FUNCTIA DE COPIERE PRIN ATRIBUIRE lista_2 = lista_1  ")
    lista_1 = [{"unu": 10, "doi": 20, "trei": 30}, {"unu": 40, "doi": 50, "trei": 60}]
    lista_2 = lista_1

    print("lista 1", lista_1)
    print("lista 2", lista_2)
    print("adresa lista 1", id(lista_1))
    print("adresa lista 2", id(lista_2))
    print("adresa lista1[0]", id(lista_1[0]))
    print("adresa lista2[0]", id(lista_2[0]))

    lista_1[0]['unu'] = -4
    print("lista 1", lista_1)
    print("lista 2", lista_2)
    print("ADRESA DE START A LISTEI ESTE ACEEASI  !!!")
    print("ADRESA DE START A SUBLISTELOR ESTE ACEEASI !!!")


def test3():
    print("test 3 : FUNCTIA DE COPIERE PRIN ATRIBUIRE lista_2 = lista_1[:]  ")
    lista_1 = [{"unu": 10, "doi": 20, "trei": 30}, {"unu": 40, "doi": 50, "trei": 60}]
    lista_2 = lista_1[:]

    print("lista 1", lista_1)
    print("lista 2", lista_2)
    print("adresa lista 1", id(lista_1))
    print("adresa lista 2", id(lista_2))
    print("adresa lista1[0]", id(lista_1[0]))
    print("adresa lista2[0]", id(lista_2[0]))

    lista_1[0]['unu'] = -4
    print("lista 1", lista_1)
    print("lista 2", lista_2)
    print("ADRESA DE START A LISTEI ESTE DIFERITA. ...OK")
    print("ADRESA DE START A SUBLISTELOR ESTE ACEEASI !!!")


def test4():
    print("test 4 : FUNCTIA COPIERE PRIN ATRIBUIRE = lista_1.copy()  ")
    lista_1 = [{"unu": 10, "doi": 20, "trei": 30}, {"unu": 40, "doi": 50, "trei": 60}]
    lista_2 = lista_1.copy()

    print("lista 1", lista_1)
    print("lista 2", lista_2)
    print("adresa lista 1", id(lista_1))
    print("adresa lista 2", id(lista_2))
    print("adresa lista1[0]", id(lista_1[0]))
    print("adresa lista2[0]", id(lista_2[0]))

    lista_1[0]['unu'] = -4
    print("lista 1", lista_1)
    print("lista 2", lista_2)
    print("ADRESA DE START A LISTEI ESTE DIFERITA. ...OK")
    print("ADRESA DE START A SUBLISTELOR ESTE ACEEASI !!!")


def test5():
    print("test 5 : FUNCTIA DE COPIERE deepcopy()    lista_2 = copy.deepcopy(lista_1)  ")
    lista_1 = [{"unu": 10, "doi": 20, "trei": 30}, {"unu": 40, "doi": 50, "trei": 60}]
    lista_2 = copy.deepcopy(lista_1)

    print("lista 1", lista_1)
    print("lista 2", lista_2)
    print("adresa lista 1", id(lista_1))
    print("adresa lista 2", id(lista_2))
    print("adresa lista1[0]", id(lista_1[0]))
    print("adresa lista2[0]", id(lista_2[0]))

    lista_1[0]['unu'] = -4
    print("lista 1", lista_1)
    print("lista 2", lista_2)
    print("ADRESA DE START A LISTEI ESTE DIFERITA. ...OK")
    print("ADRESA DE START A SUBLISTELOR ESTE DIFERITA. ...OK")


def start():
    test1()
    print("------------------------------------------------------------")
    test2()
    print("------------------------------------------------------------")
    test3()
    print("------------------------------------------------------------")
    test4()
    print("------------------------------------------------------------")
    test5()
    print("------------------------------------------------------------")
    print("Functioneaza la fel ca la LISTE DE LISTE")


if __name__ == '__main__':
    start()
