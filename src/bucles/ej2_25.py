#
#   Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
#

def introducir_frase():

    frase = None

    while frase == None:
        
        try:
            frase = input("Introduce una frase: ")

            if len(frase) < 1:
                frase = None
                e = IndexError("La frase debe tener al menos una palabra.")
                raise e
        
        except ValueError:
            print("*ERROR* Formato incorrecto")

        except IndexError:
            print(f"*ERROR* {e}")
    
    return frase

def comprobar_palabras(frase: str):

    palabras = frase.split()
    palabra_larga = ""
    num_palabras = 0

    for palabra in palabras:

        if len(palabra) >  len(palabra_larga):

            palabra_larga = palabra 

    num_palabras += 1

    return palabra_larga, num_palabras

def main():

    frase = introducir_frase()

    palabra_larga, num_palabras = comprobar_palabras(frase)

    print(f"El número de palabras ha sido {num_palabras} y la palabra más larga de la frase es {palabra_larga}")

if __name__ == "__main__":
    main()