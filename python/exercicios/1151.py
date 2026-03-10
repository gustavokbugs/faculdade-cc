def fibonacci(n, memo):
    if memo[n] != -1:
        return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


def gerar_sequencia(n):
    memo = [-1] * n

    if n > 0:
        memo[0] = 0
    if n > 1:
        memo[1] = 1

    resultado = []

    for i in range(n):
        resultado.append(str(fibonacci(i, memo)))

    print(" ".join(resultado))


def main():
    n = int(input())
    gerar_sequencia(n)


main()
