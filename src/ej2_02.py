#
#
#


def contar_edad(edad: int):
    i = None
    cadena = ""
    for i in range (1, edad + 1):
        cadena +=  str(i) + "\n"
    return cadena

def introducir_edad() -> int:
    edad = None
    while edad is None:
        try:
            edad = int(input("Introduce tu edad: "))
            if edad == None:
                edad = None
                raise ValueError
            if edad < 0 or edad > 125:
                edad = None
                raise ValueError

        except ValueError:
            print("**ERROR** Algo ha ido mal, inténtalo de nuevo...")
    return edad

def main():
    edad = introducir_edad()
    print(contar_edad(edad))

if __name__ == "__main__":
    main()