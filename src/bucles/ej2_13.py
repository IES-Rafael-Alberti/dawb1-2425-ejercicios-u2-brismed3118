#
#
#
def obtener_input():
    texto = input("Introduce algo (escribe 'salir' para terminar): ")
    return texto

def mostrar_eco(texto):
    print("Eco:", texto)

def main():
    algo = True
    while algo:
        texto = obtener_input()
        if texto.lower() == "salir":
            break
        mostrar_eco(texto)

if __name__ == "__main__":
    main()