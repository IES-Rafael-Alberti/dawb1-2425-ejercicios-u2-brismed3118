#
#
#

def mostrar_menu():

    print("\nMenú:")
    print("1. Comenzar programa")
    print("2. Imprimir listado")
    print("3. Finalizar programa")

def iniciar_programa():
    print("\nSe ha iniciado programa...")

def listado():
    print("\nEste es el listado que se imprime.")

def main():

    flag = True

    while flag == True:
        mostrar_menu()
        try:
            opcion = input("\nSelecciona una opción > ")
            
            if opcion == "1":
                iniciar_programa()

            elif opcion == "2":
                listado()

            elif opcion == "3":
                print("Finalizando el programa...")
                break 

            else:
                e = ValueError("El número introducido no es una opción.")
                raise e
        except ValueError as e:
            print(f"*ERROR* {e}")

if __name__ == "__main__":
    main()