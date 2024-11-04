#
#
#

def leer_numero_positivo():
    numero = None
    while numero == None:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            if numero < 0:
                e = IndexError("El número debe ser positivo...")
                raise e
            return numero
        
        except ValueError:
            print("*ERROR* El formato no es correcto")

        except IndexError as e:
            print(f"*ERROR* {e}")

def sumar_numero(numero):
    suma = 0
    for i in str(numero):
        suma += int(i)
    return suma

def main():
    numero = leer_numero_positivo()
    suma = sumar_numero(numero)
    print(f"La suma de los dígitos de  {numero} es: {suma}")

if __name__ == "__main__":
    main()