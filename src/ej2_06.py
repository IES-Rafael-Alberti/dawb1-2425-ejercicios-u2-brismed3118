#
#
#

def hacer_piramide(num:int) -> str:

    i = None
    piramide = ""
    secuencia = ""

    for i in range (1, num + 1):
        secuencia = "*" + secuencia
        
        if i != num:
            piramide = piramide + secuencia  + "\n"
        else:
            piramide = piramide + secuencia

    return piramide


def obtener_num() -> int:
    num = None

    while num == None:
        try:
            num = int(input("Intrduce un número para hacer el triángulo: "))
            primer_dig = str(num)[0]

            if primer_dig == "-":
                num = None
                raise ValueError
        
        except ValueError:
            print("No es un número válido")
    return num

def main():
    num = obtener_num()
    piramide = hacer_piramide(num)
    print(piramide)


if __name__ == "__main__":
    main()