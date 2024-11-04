#
#
#

def introducir_edad():
    edad = None

    while edad == None:

        try:
            edad = int(input("Introduce tu edad: "))

            if edad < 0 or edad > 125:

                edad = None
                e = IndexError("La edad no puede ser menor que 0 o mayor que 125 años.")
                raise e
        
        except ValueError:
            print("*ERROR* El formato no es válido.")

        except IndexError as e:
            print(f"*ERROR* {e}")

    return edad

def anios_cumplidos(edad: int):

    cumplidos = ""

    for i in range (1, edad + 1):

        if i != edad:
            cumplidos += str(i) + ", "

        else:
            cumplidos += str(i)
    
    return cumplidos      

def main():
    edad = introducir_edad()
    print(anios_cumplidos(edad))

if __name__ == "__main__":
    main()