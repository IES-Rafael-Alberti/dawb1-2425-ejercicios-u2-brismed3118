#
#
#

def darlavuelta(palabra:str ) -> str:
    letra = ""
    cadena = ""
    ultima = palabra[-1]
    for letra in palabra[::-1]:
        if letra == ultima:
            cadena = cadena + letra
        else:
            cadena = cadena + "\n" + letra

    return cadena

def obtener_palabra() -> str:
    word = None
    while word == None:
        try:
            word = input("Introduce una palabra: ")
            if word == "":
                word = None
                raise ValueError
        except ValueError:
            print("**ERROR** Algo ha ido mal...")

    return word

def main():
    palabra = obtener_palabra()
    print(darlavuelta(palabra))

if __name__ == "__main__":
    main()