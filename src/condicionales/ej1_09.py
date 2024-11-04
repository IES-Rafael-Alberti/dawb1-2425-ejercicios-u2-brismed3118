#
#
#

def calcular_precio(edad:int):
    if edad < 4:
        return 0
    elif 4 <= edad <= 18:
        return 5
    else:
        return 10
    
def introducir_edad():
    edad = None

    while edad is None:
        try:
            edad = int(input("Por favor, introduce la edad del cliente: "))
        except ValueError:
            print("Esa edad no es válida")
            edad = None

    return edad 


def main():
    edad = introducir_edad()
    precio = calcular_precio(edad)
    print(f"El precio de la entrada es: {precio}€")

if __name__ == "__main__":
    main()