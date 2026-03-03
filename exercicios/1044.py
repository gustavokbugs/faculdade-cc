def valida_multiplos(a, b):
    return a % b == 0 or b % a == 0


def main():

    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    if valida_multiplos(a, b):
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")


if __name__ == "__main__":
    main()
