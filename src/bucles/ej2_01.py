#
#
#

def repetir_palabra(palabra: str):
    i = None
    for i in range (0,10):
        print(palabra)

def introducir_palabra() -> str:
    palabra = None
    while palabra is None:
        try:
            palabra = input("Introduce la palabra que quieras: ")
            if palabra == "":
                palabra = None
                raise ValueError

        except ValueError:
            print("**ERROR** Algo ha ido mal, inténtalo de nuevo...")
    return palabra

def main():
    palabra = introducir_palabra()
    repetir_palabra(palabra)


if __name__ == "__main__":
    main()