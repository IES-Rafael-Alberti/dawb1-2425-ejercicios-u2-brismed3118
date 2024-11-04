#
#
#

def contar_num(num: int):
    i = None
    cadena = ""
    for i in range (0, num + 1):

        if i == 0:
            cadena = str(i)
        else:
            cadena = str(i) + ", " + cadena 

    return cadena

def introducir_num() -> int:
    num = None
    while num is None:
        try:
            num = int(input("Introduce un número positivo: "))
            if num == None:
                num = None
                raise ValueError
            if num < 0:
                num = None
                raise ValueError

        except ValueError:
            print("**ERROR** Algo ha ido mal, inténtalo de nuevo...")
    return num

def main():
    num = introducir_num()
    print(contar_num(num))

if __name__ == "__main__":
    main()