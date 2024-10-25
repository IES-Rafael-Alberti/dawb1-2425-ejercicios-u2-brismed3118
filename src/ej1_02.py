#
#   SIN TERMINAR
#

def comprueba_contrasenia(pswd:str, entrada:str) -> bool:
    
    if pswd == entrada:
        return True
    else:
        return False
    
def main():
   pswd = "contraseña"
   entrada = input("Introduzca la contraseña > ").lower()
   if comprueba_contrasenia(pswd, entrada) == True:
       print("Contraseña correcta")
   else:
       print("Contraseña incorrecta...")
       


if __name__ == "__main__":
    main()