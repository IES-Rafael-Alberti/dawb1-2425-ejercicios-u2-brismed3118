#
#
#

def introducir_frase():
    frase = None

    while frase == None:
        try:
            frase = input("Introduce una frase: ")

            if len(frase) < 1:
                frase = None
                raise ValueError("Introduce una frase.")
            
            return frase

        except ValueError as e:
            print(f"*ERROR* {e}")

def introducir_letra():
    letra = None

    while letra == None:
        try:
            letra = input("Introduce una letra: ")

            if len(letra) > 1:
                letra = None
                raise ValueError("Introduce solo una letra.")

            return letra
        
        except ValueError as e:
            print(f"*ERROR* {e}")

def encontrar_letra(letra: str, frase: str):
    posicion = 0
    for i in frase:

        if i == letra:

            print(f"La letra {letra} se encuentra en en la posición {posicion}.")
            break

        else:
            print(f"No se encuentra la letra {letra} en la posición {posicion}.")
        
        posicion += 1


def main():
    letra = introducir_letra()
    frase = introducir_frase()
    encontrar_letra(letra, frase)

if __name__ == "__main__":
    main()


            