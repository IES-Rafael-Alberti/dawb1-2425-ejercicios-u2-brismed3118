#
#
#

def verificar_contrasenia():

    contrasenia_correcta = "contraseña"

    try:

        contrasenia_ingresada = input("Por favor, ingrese la contraseña: ")

        if contrasenia_ingresada != contrasenia_correcta:
            raise NameError("Incorrect Password!!")
        
        print("Contraseña correcta.")
            
    except NameError as e:
        print(e)

def main():
        
        verificar_contrasenia()



if __name__ == "__main__":
    main()
