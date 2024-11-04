#
#
#

def division(num1: float, num2:float) -> float:
    div = num1 / num2
    return div

def main():
    num1 = float(input("Introduce el primer número"))
    num2 = float(input("Introduce el segundo número"))

    if num2 == 0 :
        print("**ERROR**")

    else:
       print(division(num1, num2))


if __name__ == "__main__":
    main()