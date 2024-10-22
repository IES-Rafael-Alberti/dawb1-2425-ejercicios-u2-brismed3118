#
#
#

def comprobar_num():
    flag = True
    num = numero()
    while  num.lower() != "fin":
        try:
            num = int(num)
            print(num)
            num = numero()
        except ValueError:
            print("Lo siento ese no es número válido... Inténtalo de nuevo")
            num = numero()
    return num

def numero():
    num = input("Introduce un número: ")
    return num

def bucle():
    flag = True
    while flag:
        entrada = comprobar_num()
        if entrada.lower != 'fin':
            flag = False
        print(entrada)
   
    return

def main():
    bucle()
    print('¡Terminado!')

if __name__ == "__main__":
    main()