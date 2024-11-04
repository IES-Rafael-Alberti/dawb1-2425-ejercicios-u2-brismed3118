#
#
#

def letraenfrase(frase: str, letra: str) -> int:

    veces = 0

    for i in frase:
        
        if i == letra:
            veces += 1
    
    return veces
def obtener_frase():
    frase = False

    while frase == False:
        try: 
            frase = input("Introduce una frase: ")
            if frase == "":
                e = ValueError("No puede estar vacío")
                raise e
        except ValueError as e:
            frase = False
            print(f"*ERROR*{e}")
            
    return  frase

def obtener_letra():

    letra = False

    while letra == False:
        try: 
            letra = input("Introduce una letra: ")

            if len(letra) > 1:
                e = ValueError("Solo puedes introducir una letra")
                raise e
            
            if letra == "":
                e = ValueError("No puede estar vacío")
                raise e
        except ValueError as e:
            letra = False
            print(f"*ERROR*{e}")
            
    return  letra

def main():

    frase = obtener_frase()
    letra = obtener_letra()
    print(f"La letra ({letra}) se repite {letraenfrase(frase, letra)} veces en la frase")

if __name__ == "__main__":
    main()