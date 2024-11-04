#
#
#

def comprobar_contra(entrada: str, contrasenia: str) -> bool:
    if entrada != contrasenia:
        return False
    else:
        return True

def obtener_input() -> str:
    contra = None
    while contra == None:
        try:
            contra = input("Introduce la contraseña: ")
            if contra == "":
                contra = None
                raise ValueError
        except ValueError:
            print("**ERROR** Formato incorrecto, inténtelo de nuevo...")
    return contra
def main():
    contrasenia = "contraseña"
    entrada = obtener_input()
    while comprobar_contra(entrada, contrasenia) == False:  
        print("La contraseña es incorrecta...")
        entrada = obtener_input()

    print("La contraseña es correcta")

if __name__ == "__main__":
    main()