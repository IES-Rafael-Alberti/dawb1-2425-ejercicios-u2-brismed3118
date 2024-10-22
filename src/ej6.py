#
#
#

def comprobar_grupo(nombre: str, sexo: str):
    
    letra_f = "m"
    letra_m = "n"
    if sexo == "f":
        if ord(nombre) < ord(letra_f):
            print("Correspondes al grupo A...")
        else:
            print("Correspondes al grupo B...")
    else:
        if ord(nombre) > ord(letra_m):
            print("Correspondes al grupo A...")
        else:
            print("Correspondes al grupo B...") 

def obtener_nombre():
    nombre = input("Introduzca su nombre: ").lower()
    primera_letra = nombre[0]
    return primera_letra

def obtener_sexo():
    sexo = input("Introduzca el sexo [m/f]: ")

    while sexo != "f" and sexo != "m":
        print("**ERROR** No válido, inténtalo de nuevo.")
        sexo = input("Introduzca el sexo [m/f]: ")
    return sexo

def main():
    nombre = obtener_nombre()
    sexo = obtener_sexo()
    comprobar_grupo(nombre, sexo)

if __name__ == "__main__":
    main()