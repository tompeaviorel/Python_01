def calcul(a, b, operatie) -> float:
    if operatie == '+':
        return a + b
    elif operatie == '-':
        return a - b
    elif operatie == '*':
        return a * b
    elif operatie == '/':
        return a / b


def meniu():
    while True:
        cmd = input(">>> (de forma 2 + 3) ")
        if cmd == 'exit':
            break
        token = cmd.split()
        if len(token) > 3:
            print("comanda gresita")
        else:
            a = int(token[0])
            b = int(token[2])
            op = token[1]
            print(calcul(a, b, op))


if __name__ == '__main__':
    print("start")
    meniu()
    