
def citeste_1():
    x = int(input("n = "))
    if x < 0:
        raise Exception("Prea mic")
    if x > 9:
        raise Exception("Prea mare")
    return x


def start():
    print("Citim o cifra. Ce se intampla daca nu introduc o cifra? ")
    print("Cazul 1: 4")
    print("Cazul 2: -5")
    print("Cazul 3: 18")
    print("Cazul 4: 45ab")
    try:
        n = citeste_1()
    except ValueError:
        print("ati introdus si alte caractere in afara de cifre ")
        print('instructiunea :  int(input("n = ")) ')
        print("a generat automat o exceptie de tip ValueError ")
    except Exception as msg:
        print(msg)
    else:
        print("Corect ", n)
    finally:
        print("Secventa s-a terminat.....intr-un fel sau altul")


if __name__ == '__main__':
    start()


"""
In limbajul Python, toate exceptiile sunt instante ale unor clase derivate din BaseException. 
Clasele corespunzatoare exceptiilor sunt definite prin intermediul unei ierarhii de clase.

BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
In plus, fata de beneficiile organizationale evidente, utilizarea acestei ierarhii este utila in tratarea exceptiilor. 
Tratarea unei exceptii de un anumit tip presupune si tratarea exceptiilor derivate din acest tip de exceptie.

Tratarea exceptiilor
Limbajul Python ofera o solutie eficienta de rezolvare a exceptiilor care apar intr-un program prin intermediul 
mecanismului de tratare a exceptiilor. 
Implementarea acestei solutii se face folosind constructii de tipul try .. except .. finally.

try:
    # instructiuni urmarite
except Exceptie:
    # tratare exceptii de tip Exceptie
...
except:
    # tratare pentru restul exceptiilor
else:
    # instructiuni executate daca nu sunt generate exceptii
finally:
    # instructiuni executate neconditionat
"""