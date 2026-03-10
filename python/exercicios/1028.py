def calcular_mdc(a, b):
    if b == 0:
        return a
    return calcular_mdc(b, a % b)


def processar_casos():
    n = int(input())

    for _ in range(n):
        f1, f2 = map(int, input().split())
        resultado = calcular_mdc(f1, f2)
        print(resultado)


def main():
    processar_casos()


main()
