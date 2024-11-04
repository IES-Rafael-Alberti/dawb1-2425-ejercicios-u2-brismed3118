#
#
#

def mostrar_inversion(inv: int, interes: int, anios: int) -> str:
    i = None
    capital = inv
    todo = ""

    for i in range (1, anios + 1):
        capital *= 1 + interes / 100
        obtenido = float(capital) - float(inv)
        if i != anios:
            todo += f"El año {i} recibirá " + str(obtenido) + "€\n"
        else:
            todo += f"El año {i} recibirá " + str(obtenido) + "€"

    return todo
        

def introducir_anios() -> int:
    anios = None
    while anios is None:
        try:
            anios = int(input("Introduce los años de años que dura la inversión: "))
            if anios == None:
                anios = None
                raise ValueError
            if anios < 0:
                anios = None
                raise ValueError

        except ValueError:
            print("**ERROR** Algo ha ido mal, inténtalo de nuevo...")
    return anios

def introducir_interes() -> int:
    interes = None
    while interes is None:
        try:
            interes = int(input("Introduce un el interés anual: "))
            if interes == None:
                interes = None
                raise ValueError
            if interes < 0:
                interes = None
                raise ValueError

        except ValueError:
            print("**ERROR** Algo ha ido mal, inténtalo de nuevo...")
    return interes

def introducir_inv() -> int:
    inv = None
    while inv is None:
        try:
            inv = int(input("Introduce la cantidad a invertir: "))
            if inv == None:
                inv = None
                raise ValueError
            if inv < 0:
                inv = None
                raise ValueError

        except ValueError:
            print("**ERROR** Algo ha ido mal, inténtalo de nuevo...")
    return inv

def main():
    inv = introducir_inv()
    interes = introducir_interes()
    anios = introducir_anios()
    print(mostrar_inversion(inv, interes, anios))

if __name__ == "__main__":
    main()