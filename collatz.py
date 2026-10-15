
# Calculando el número de iteraciones del algoritmo de Collatz
def collatz(num):
    iteraciones = 0

    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1

        iteraciones += 1

    return iteraciones


def main():
    try:
        numero = int(input("Ingrese un número entre 1 y 1999: "))

        if numero < 1 or numero > 1999:
            print("Número inválido")
            return

        resultado = collatz(numero)

        print(
            f"El número de iteraciones para {numero} "
            f"es {resultado}"
        )

    except ValueError:
        print("Número inválido")


if __name__ == "__main__":
    main()
