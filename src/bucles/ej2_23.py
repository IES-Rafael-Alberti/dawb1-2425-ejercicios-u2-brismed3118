#
#   Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.
#

def introducir_linea():

    linea = None

    while linea == None:
        try:
            linea = input("Libro: ")

            if linea == "":
                linea = None
                e = IndexError("El campo no puede estar vacío. ")
                raise e

        except IndexError as e:
            print(f"*ERROR* {e}")

        except ValueError:
            print("*ERROR* Algo ha ido mal...")
    
    return linea

def contar_titulo(titulo):

    digitos = 0

    for i in titulo:

        for x in range(0,10):

            if str(i) == str(x):
                
                digitos += 1

    return digitos

def main():

    titulo = ""
    linea = ""
    lineas_completas = 0

    while linea != "*":

        linea = introducir_linea()

        if linea == "/":
            
            print(f"Línea completa. Aparecen {contar_titulo(titulo)} dígitos numéricos.")
            lineas_completas += 1
            titulo = ""

        else:
            titulo += linea
    
    print(f"El total de líneas completas introducidas es {lineas_completas}")

if __name__ == "__main__":
    main()