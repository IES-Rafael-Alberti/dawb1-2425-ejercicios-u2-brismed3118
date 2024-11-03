#
#
#

def leer_numero():

    numero = None

    while numero == None:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            if numero < -1:
                e = IndexError("El número debe ser positivo o diferente a -1")
                raise e
            return numero
        
        except ValueError:
            print("*ERROR* El formato no es correcto")

        except IndexError as e:
            print(f"*ERROR* {e}")

def sumar_numeros(numero):

    suma = 0

    for i in str(numero):
        suma += int(i)
        
    return suma

def main():

    contador_pares = 0
    flag = True

    while flag:
        numero = leer_numero()
        
        if numero == -1:
            break

        suma = sumar_numeros(numero)
        print(f"La suma de los dígitos de {numero} es: {suma}")
        
        if numero % 2 == 0:
            contador_pares += 1

    print(f"Se han introducido {contador_pares} números pares.")

if __name__ == "__main__":
    main()