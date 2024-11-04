#
#
#

def calcular(i: int) -> str:

    total = i * 10
    return total


def tabla_diez() -> str:

    i = None
    tabla = ""
    calculo = ""
    
    for i in range (0, 11):

        calculo = "10 x " + str(i) + " = " + str(calcular(i))
        if i != 10:
            tabla += calculo + "\n"
        else:
            tabla += calculo

    return tabla

def main():
    print(tabla_diez())

if __name__ == "__main__":
    main()